def func_counter(func):
    def wrapper():
        counter = 0
        func()
        counter += 1
    return wrapper()

