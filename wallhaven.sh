#!/usr/bin/env bash

python3 havenscraper.py
# shellcheck disable=SC2012
wal -i "$(ls -Art downloads | tail -n 1)"