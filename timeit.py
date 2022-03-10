import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        delay = end - start
        print("Total Time " + delay)
    return wrapper
