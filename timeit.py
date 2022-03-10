import time
def calculate_time(func):
    
    def wrapper():
        timeOne = time.time()
        func()
        timeTwo = time.time()
        total = timeTwo - timeOne
        print("Total time %s" % total)
    return wrapper

@calculate_time
def timeOf(): 
    print("")
    
timeOf()



