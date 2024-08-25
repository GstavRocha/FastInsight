#!/bin/bash

echo "chouse the virtual env"

source env-pymongo-fastapi/bin/activate

TESTE=$(pwd)
echo "PYTHONPATH=$TESTE"
export PYTHONPATH=$TESTE
echo "It is OK"