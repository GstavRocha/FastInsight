from cronometer import execution_time   
import subprocess
import time

def database_status():
    try:
        time.sleep(5)
    finally:
        time

@execution_time
def load_server():
    print('Server Reload')
    subprocess.run(['uvicorn main:app --reload'], shell=True)
    for i in range(1000000):
        pass 
            
if __name__ == '__main__':
    print("Start Serve")
    subprocess.run(['systemctl start mongod'], shell= True)
    load_server()