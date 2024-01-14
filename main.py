import timeit
import random
from tabulate import tabulate
from insertion_sort import insertion_sort
from merge_sort import merge_sort


def measure_time(algorithm, data):
    return timeit.timeit(lambda: algorithm(data[:]), number=10)


if __name__ == "__main__":
    small_dataset = random.sample(range(1, 100), 10)
    medium_dataset = random.sample(range(1, 1000), 100)
    large_dataset = random.sample(range(1, 10000), 1000)

    sorting_algorithms = [
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
        ("Time sort", sorted),
        ("Time sort speedup", list.sort),
    ]

    table = [
        [name] + [measure_time(algorithm, data) for data in (small_dataset, medium_dataset, large_dataset)]
        for name, algorithm in sorting_algorithms
    ]

    headers = ["Algorithm", "Time small data", "Time medium data", "Time large data"]

    print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".8f"))
