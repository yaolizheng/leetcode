#!/usr/bin/bash
filename="$1"
(tr ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}') < $filename
