def has_duplicate(n):
    hash_set = set()
    for x in n:
        if x in hash_set:
            return True
        hash_set.add(x)
    return False


if __name__ == '__main__':
    n = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    n = [1, 2, 3, 4]
    print has_duplicate(n)
