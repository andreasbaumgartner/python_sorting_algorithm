from random import randint
from timeit import repeat


def run_algo(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def gen_array(n: int = 1000):
    return [randint(0, 1000) for _ in range(n)]
