def knows(a, b):
    pass


def celebrity(n):
    candidate = 0
    for i in range(n):
        if knows(candidate, i):
            i = candidate
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate


if __name__ == '__main__':
    print celebrity(10)
