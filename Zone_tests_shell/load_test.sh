#! /bin/bash
SCRIPT_PATH="uvicorn main:app --host 127.0.0.1 --port 8000"
sudo -v


$SCRIPT_PATH &


sleep 5


UVICORN_PID=$(lsof -t -i:8000)


if [ -z "$UVICORN_PID" ]; then
    echo "Uvicorn server not found on port 8000."
    exit 1
fi
x
echo "Uvicorn PID: $UVICORN_PID"
for i in {1..10}
do  
    echo "Run $i"
    time $SCRIPT_PATH
done
kill -SIGKILL $UVICORN_PID
echo "Uvicorn server stopped."