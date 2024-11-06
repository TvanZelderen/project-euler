import timeit

from problems import problem35

if __name__ == "__main__":
    start = timeit.default_timer()

    print(problem35.solve())

    stop = timeit.default_timer()
    print(f"Runtime: {stop - start}")
