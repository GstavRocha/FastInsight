#!/bin/bash
URL="http://127.0.0.1:8000/"
echo "link $URL"
for i in {1..10}
do
   START_TIME=$(date +%s%N)
   curl -s -o /dev/null $URL
   END_TIME=$(date +%s%N)
   ELAPSED_TIME=$(( ($END_TIME - $START_TIME) / 1000000 ))
   echo "Request $i took $ELAPSED_TIME ms"
done