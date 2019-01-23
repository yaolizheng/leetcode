def is_utf8(l):
    i = 0
    while i < len(l):
        if l[i] < 128:
            i += 1
            continue
        else:
            count = 0
            x = l[i]
            for j in range(7, 0, -1):
                if x >= 2**j:
                    count += 1
                else:
                    break
                x -= 2**j
            if count == 1:
                return False
            for j in range(i + 1, i + count):
                if l[j] < 128 or l[j] > 191:
                    return False
            i += count - 1
        i += 1
    return True


if __name__ == '__main__':
    data = [197, 130, 1]
    print is_utf8(data)
