#!/bin/bash
#chmod 755 script.sh
for number in {0..10}
do
    ping -q www.google.com -c 1 > /dev/null &
done
wait
exit 0
