import time
def calculate_time(func):
    def wrapper():
        begin = time.time()
        func()
        term = time.time()
        delay = term - begin
        print("Total Time %s" % delay)
    return wrapper

@calculate_time
def run1(): 
    print("")


