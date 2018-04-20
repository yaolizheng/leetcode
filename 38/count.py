def count_say(num):
    if num == 1:
        return '1'
    prev = None
    count = 0
    rv = ''
    for i in count_say(num - 1):
        if prev is None:
            prev = i
            count = 1
        elif i != prev:
            rv += (str(count) + prev)
            count = 1
            prev = i
        else:
            count += 1
    return rv + (str(count) + prev)


if __name__ == '__main__':
    num = 5
    print count_say(num)
