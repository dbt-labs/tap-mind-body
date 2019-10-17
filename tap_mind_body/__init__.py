#!/usr/bin/env python3

import singer

import tap_framework

from tap_mind_body.client import MindBodyClient
from tap_mind_body.streams import AVAILABLE_STREAMS

from tap_framework.streams import is_selected
from tap_framework.state import save_state

LOGGER = singer.get_logger()  # noqa


class MindBodyRunner(tap_framework.Runner):
    def get_streams_to_replicate(self):
        streams = []

        if not self.catalog:
            return streams

        stream_map = {}
        for stream_catalog in self.catalog.streams:
            if not is_selected(stream_catalog):
                LOGGER.info("'{}' is not marked selected, skipping."
                            .format(stream_catalog.stream))
                continue

            for available_stream in self.available_streams:
                if available_stream.matches_catalog(stream_catalog):
                    if not available_stream.requirements_met(self.catalog):
                        raise RuntimeError(
                            "{} requires that that the following are "
                            "selected: {}"
                            .format(stream_catalog.stream,
                                    ','.join(available_stream.REQUIRES)))

                    to_add = available_stream(
                        self.config, self.state, stream_catalog, self.client
                    )

                    stream_map[to_add.TABLE] = to_add
                    streams.append(to_add)

        # Add substreams to the stream instances
        for stream in streams:
            for parent in stream.REQUIRES:
                stream_map[parent].substreams.append(stream)

        return streams

    def do_sync(self):
        LOGGER.info("Starting sync.")

        streams = self.get_streams_to_replicate()

        for stream in streams:
            # Don't sync substreams directly -- sync them
            # via their parents
            if len(stream.REQUIRES) > 0:
                continue

            try:
                stream.state = self.state
                stream.sync()
                self.state = stream.state
            except OSError as e:
                LOGGER.error(str(e))
                exit(e.errno)

            except Exception as e:
                LOGGER.error(str(e))
                LOGGER.error('Failed to sync endpoint {}, moving on!'
                             .format(stream.TABLE))
                raise e

        save_state(self.state)


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=[
        'api_key',
        'site_id'])
    client = MindBodyClient(args.config)
    runner = MindBodyRunner(args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
