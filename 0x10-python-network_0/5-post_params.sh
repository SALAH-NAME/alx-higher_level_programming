#!/bin/bash
# 5-post_params.sh

curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
