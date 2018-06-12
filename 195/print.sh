#!/user/bin/bash
filename=$1
awk '{ if (FNR==10) print $0 }' $filename
