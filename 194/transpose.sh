#!/usr/bin/bash
filename="$1"
for i in `seq 1 $(head -1 $filename | wc -w)`; do awk -v I=$i '{print $I}' $filename | tr '\n' ' '; echo; done;
