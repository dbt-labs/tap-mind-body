#!/bin/bash

### Load configuration
echo "$STITCH_CONFIG" > persist.json || { echo "Missing stitch config!"; exit 1; }
echo "$TAP_CONFIG" > config.json || { echo "Missing tap config!"; exit 1; }
echo "$CATALOG" > catalog.json || { echo "Missing catalog!"; exit 1; }

aws s3 cp "$TAP_STATE_FILE_S3_PATH" state.json || echo "{}" > state.json

### Run the tap
{ tap-mind-body -s state.json -c config.json --catalog catalog.json | target-stitch -c persist.json > state.log; }

tail -n1 state.log > new-state.json

### Save state file
if [ -s new-state.json ]
then
    aws s3 cp new-state.json "$TAP_STATE_FILE_S3_PATH"
fi