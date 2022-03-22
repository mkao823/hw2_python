def func_counter(func):
    counter = 0
    def wrapper():
        func()
        counter += 1
    return wrapper()

