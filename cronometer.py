import time

def execution_time(param):
    def wrapper(*arg, **kwargs):
        initial_time = time.time()
        result = param(*arg, **kwargs)
        end = time.time()
        total_time = end - initial_time
        print(f'Time To process {total_time: .4f} segundos')
        return result
    return wrapper

            