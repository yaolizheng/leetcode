#!/usr/bin/bash
filename="$1"
grep -P '^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$' $filename
