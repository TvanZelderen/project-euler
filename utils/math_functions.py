def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """Calculate factorial numbers from n."""
    if n > 0:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    elif n == 0:
        return 1
    else:
        raise (ValueError("n should be a positive int."))


def factorial_0_to_9() -> list[int]:
    """Precalculate factorials for single digits."""
    factorials = [factorial(i) for i in range(10)]
    return factorials


if __name__ == "__main__":
    print(factorial_0_to_9())
