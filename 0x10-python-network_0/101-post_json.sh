#!/bin/bash
# 101-post_json.sh

curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
