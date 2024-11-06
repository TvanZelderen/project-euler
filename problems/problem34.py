from utils.math_functions import factorial, factorial_0_to_9


def digit_factorial(n: int) -> bool:
    number_string = str(n)
    sum = 0
    for number in number_string:
        sum += factorial(int(number))
    return sum


def digit_factorial_precalc(n: int, factorials: list[int]) -> int:
    return sum(factorials[int(digit)] for digit in str(n))


def solve():
    sum = 0
    upper_bound = 99999
    for i in range(10, upper_bound):
        if i == digit_factorial(i):
            sum += i
    return sum


def solve_precalc():
    sum = 0
    upper_bound = 99999
    factorials = factorial_0_to_9()
    for i in range(10, upper_bound):
        if i == digit_factorial_precalc(i, factorials):
            sum += i
    return sum


def example():
    print(digit_factorial(145))
