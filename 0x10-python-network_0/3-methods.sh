#!/bin/bash
# 3-methods.sh

curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
