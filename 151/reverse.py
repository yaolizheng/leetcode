def reverse(s):
    return ' '.join(reversed(s.split(' ')))


if __name__ == '__main__':
    s = "the sky is blue"
    print reverse(s)
