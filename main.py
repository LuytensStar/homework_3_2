import time
from multiprocessing import Pool, cpu_count


def factorize(number):
    arr = []
    for i in range(1, number + 1):
        if number % i == 0:
            arr.append(i)
    return arr


numbers = [128, 255, 99999, 10651060]

a = factorize(128)
assert a == [1, 2, 4, 8, 16, 32, 64, 128]


# def parallel_factorize(numbers):
#     with ProcessPoolExecutor() as executor:
#         return list(executor.map(factorize, numbers))
def parallel_factorize(numbers):
    with Pool(cpu_count()) as p:
        return p.map(factorize, numbers)


if __name__ == "__main__":
    start = time.time()
    results = [factorize(n) for n in numbers]
    end = time.time()

    print(f"Синхронна версія: {end - start} секунд")

    start = time.time()
    results_parallel = parallel_factorize(numbers)
    end = time.time()
    print(f"Паралельна версія: {end - start} секунд")
