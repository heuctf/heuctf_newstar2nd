#!/bin/sh	
sed -i "s/orgctf{123456}/$GZCTF_FLAG/" /var/www/html/main.c
export GZCTF_FLAG=""
gcc /var/www/html/main.c -o flag.out
rm -f /var/www/html/main.c
rm -f /flag.sh