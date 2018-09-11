from collections import Counter


def is_palindrome(n):
    c = Counter(n)
    count = 0
    for key in c:
        if c[key] % 2 == 0:
            count += 1
    return count == len(c) if (len(n) % 2 == 0) else (count == len(c) - 1)


if __name__ == '__main__':
    n = 'carerac'
    print is_palindrome(n)
