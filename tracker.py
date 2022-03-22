def func_counter(func):
    count = 0
    def wrapper():
        counter = 0
        func()
        counter += 1
    return wrapper()
    count + counter

