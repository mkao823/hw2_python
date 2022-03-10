import time
def calculate_time(func):
    def wrapper():
        timeOne = time.time()
        func()
        timeTwo = time.time()
        difference = timeTwo - timeOne
        print("Total Time %s" % difference)
    return wrapper

@calculate_time
def run1(): 
    print("")

