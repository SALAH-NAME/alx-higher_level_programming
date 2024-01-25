#!/bin/bash
# 100-status_code.sh

curl -so /dev/null -w "%{http_code}" "$1"
