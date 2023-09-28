#!/bin/bash
# 0-body_size.sh
url=$1
curl -sI "$url" | grep 'Content-Length' | cut -d ' ' -f 2
