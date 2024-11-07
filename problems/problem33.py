from itertools import combinations

def combination_generator():
    numbers = [i for i in range(10, 100)]
    return list(combinations(numbers, 2))

def combination_filter():
    combinations = combination_generator()
    valid_combinations = []
    for combination in combinations:
        digit_set = set(str(combination[0]) + str(combination[1]))
        if len(digit_set) < 4:
            valid_combinations.append(combination)
    return valid_combinations

def cancelling_fractions(a, b):
    for i in range(10):
        a_str = str(a)
        b_str = str(b)
        if a_str[1] == "0" and b_str[1] == "0" and i == 0: # Trivial case
            continue
        fraction = a/b
        a_str = a_str.replace(str(i), "")
        b_str = b_str.replace(str(i), "")
        if len(a_str) == 0 or len(b_str) == 0: # A number was completely removed
            continue
        if len(a_str) == 2 and len(b_str) == 2: # The case where no digit was removed
            continue
        if int(b_str) == 0: # Dividing by zero
            continue
        if fraction == int(a_str) / int(b_str):
            print(f"Found one! a: {a}, b: {b}, fraction = {a_str} / {b_str}")

def solve():
    combinations = combination_filter()
    for numbers in combinations:
        cancelling_fractions(numbers[0], numbers[1])

def example():
    cancelling_fractions(49, 98)

if __name__ == "__main__":
    example()