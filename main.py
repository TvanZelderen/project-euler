import timeit

from problems import problem33

if __name__ == "__main__":
    start = timeit.default_timer()

    print(problem33.solve())

    stop = timeit.default_timer()
    print(f"Runtime: {stop - start}")
