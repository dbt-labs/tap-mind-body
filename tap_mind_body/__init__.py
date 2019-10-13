#!/usr/bin/env python3

import singer

import tap_framework

from tap_mind_body.client import MindBodyClient
from tap_mind_body.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class MindBodyRunner(tap_framework.Runner):
    pass


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
