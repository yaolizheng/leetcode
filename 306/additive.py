def is_additive(n):
    l = len(n)
    for i in range(1, l):
        for j in range(i + 1, l + 1):
            first = n[:i]
            second = n[i:j]
            next = str(int(first) + int(second))
            candidate = first + second + next
            while len(candidate) < len(n):
                first = second
                second = next
                next = str(int(first) + int(second))
                candidate += next
            if n == candidate:
                return True
    return False


if __name__ == '__main__':
    n = '199100199'
    print is_additive(n)
