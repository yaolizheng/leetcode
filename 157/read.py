def read4():
    test = ['1234', '5678', '9011', '11']
    for data in test:
        yield data


def read(buf, n):
    read_bytes = 0
    for buffer in read4():
        l = len(buffer)
        if l < 4 or read_bytes + 4 > n:
            bytes = min(n - read_bytes, l)
            read_bytes += bytes
            buf += buffer[:bytes]
            break
        read_bytes += len(buffer)
        buf += buffer
    return read_bytes


if __name__ == '__main__':
    buf = ""
    n = 100
    print read(buf, n)
