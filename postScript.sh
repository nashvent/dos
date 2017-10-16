#!/bin/bash
#chmod 755 script.sh
for number in {0..10}
do
    wget -qO- --post-data="user=nash&password=123" http://www.httpbin.org/post > /dev/null &
done
wait
exit 0

#-O /dev/null
