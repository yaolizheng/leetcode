def jug(x, y, z):
    return z == 0 or (x + y >= z and z % gcd(x, y) == 0)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = gcdExtended(b % a, a)
    return g, y - (b / a) * x, x


if __name__ == '__main__':
    x = 3
    y = 6
    z = 5
    print jug(x, y, z)
    a = 3
    b = 6
    print gcdExtended(a, b)
