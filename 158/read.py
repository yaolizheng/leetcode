def read4():
    test = ['1234', '5678', '9011', '11']
    for data in test:
        yield data


temp_buff = ''


def read(buf, n):
    global temp_buff
    temp_len = len(temp_buff)
    if temp_len > 0 and n <= temp_len:
        buf = temp_buff[:n]
        temp_buff = temp_buff[n:]
        print buf
        return n
    buf += temp_buff
    read_bytes = temp_len
    for buffer in read4():
        l = len(buffer)
        if l < 4 or read_bytes + 4 > n:
            bytes = min(n - read_bytes, l)
            read_bytes += bytes
            buf += buffer[:bytes]
            temp_buff = buffer[bytes:]
            break
        read_bytes += len(buffer)
        buf += buffer
    return read_bytes


if __name__ == '__main__':
    buf = ""
    n = 5
    print read(buf, n)
