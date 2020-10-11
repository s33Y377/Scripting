import time
import multiprocessing


def calc_square(result):
    numbers = [2, 3, 4]
    print("result", result)
    for x in numbers:
        result.append(x)
    result = numbers


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        result = manager.list()

    p1 = multiprocessing.Process(target=calc_square, args=(result))

    p1.start()
    p1.join()
