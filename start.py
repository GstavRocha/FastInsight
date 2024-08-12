from Database import db_conn, db_link
from cronometer import execution_time
import subprocess
import time 

@execution_time
def main():
    db_conn(db_link)
    for i in range(1000000):
        pass 
            
if __name__ == '__main__':
    subprocess.Popen(['uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8080'])
    time.sleep(2)
    main()