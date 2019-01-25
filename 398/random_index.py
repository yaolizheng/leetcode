import random


def random_index(n, k):
    res = -1
    count = 0
    for i in range(len(n)):
        if n[i] != k:
            continue
        count += 1
        if random.randint(0, count - 1) == 0:
            res = i
    return res


if __name__ == '__main__':
    n = [1, 2, 3, 3, 3]
    k = 3
    print random_index(n, k)
