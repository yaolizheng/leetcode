def num_bits(n):
    result = [0]
    for i in range(1, n + 1):
        if i % 2:
            result.append(result[i / 2] + 1)
        else:
            result.append(result[i / 2])
    return result


if __name__ == '__main__':
    n = 5
    print num_bits(n)
