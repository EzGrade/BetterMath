def product(list: list) -> int: # Product of all elements in list
    a = 1
    for i in list:
        a *= i
    return a

def factorial(a: int) -> int: # Factorial function (takes 1 int)
    return product([i for i in range(1, a + 1)])

def placement(down, up: int) -> int: # Number of all possible placement (takes 2 int, (from, to))
    return (factorial(up) / factorial(up - down))

def combinations(down, up: int) -> int: # Number of all possible combinations (takes 2 int, (from, to))
    return (factorial(up) / (factorial(up - down) * factorial(down)))

if __name__ == '__main__':
    start()