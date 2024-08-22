#! /bin/bash
for i in {1..10}
do
    echo "Test $i"
    df -h | grep 'Fylesystem\|/dev/sda1'
    free -m
    sleep 3
done