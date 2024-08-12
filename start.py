from Database import db_conn, db_link
from cronometer import execution_time
import main
import subprocess
import time

def database_status():
    try:
        time.sleep(5)
    finally:
        time

@execution_time
def load_server():
    print('Server Reloading')
    subprocess.run(['uvicorn main:app --host 0.0.0.0 --port 8080'], shell=True)
    db_conn(db_link)
    for i in range(1000000):
        pass 
            
if __name__ == '__main__':
    print("Status MongoDB Local")
    subprocess.run(['systemctl start mongod'], shell= True)
    load_server()