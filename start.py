from Database import db_conn, db_link
from cronometer import execution_time
import subprocess
import time
import threading 
def database_status():
    process = subprocess.Popen(['systemctl','status','mongod'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        time.sleep(5)
    finally:
        process.terminate()

@execution_time
def main():
    db_conn(db_link)
    for i in range(1000000):
        pass 
            
if __name__ == '__main__':
    subprocess.run(['systemctl start mongod'], shell= True)
    print("Status MongoDB Local")
    
    status_thread = threading.Thread(target=database_status)
    status_thread.start()
    subprocess.run(['systemctl status mongod'], shell= True)
    time.sleep(5)
    subprocess.run('q',shell=True)
    subprocess.Popen(['uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8080'])
    time.sleep(2)
    main()