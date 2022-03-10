import time
def calculate_time(func):
    def wrapper():
        timeOne = time.time()
        func()
        timeTwo = time.time()
        delay = timeTwo - timeOne
        print("Total Time %s" % delay)
    return wrapper

@calculate_time
def run1(): 
    print("")

run1()


