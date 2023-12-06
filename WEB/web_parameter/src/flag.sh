#!/bin/sh	
sed -i "s/orgctf{123453634634}/$GZCTF_FLAG/" /var/www/html/flag.php
export GZCTF_FLAG=""
rm -f /flag.sh