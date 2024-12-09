import cProfile

def example_function():
    total = 0
    for i in range(1000):
        total += i ** 2
    return total

cProfile.run('example_function()')
