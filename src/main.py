import time

def time_it(func):

    def inner(*args, **kwargs):
        start = time.time()
        called_func = func(*args, **kwargs)
        end = time.time()
        print(f"Duration: {end-start}.")
    
    return inner

@time_it
def loopsy(iterations: int):
    return sum([i for i in range(iterations)])

result = loopsy(100_000)
print(f"Sum is {result}")

result = loopsy(100_000)
print(f"Sum is {result}")