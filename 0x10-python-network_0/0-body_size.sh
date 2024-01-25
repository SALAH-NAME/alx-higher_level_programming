#!/bin/bash
# 0-body_size.sh

curl -s "$1" | wc -c
