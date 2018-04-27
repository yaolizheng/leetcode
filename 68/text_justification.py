import math


def justify(temp, count, max_len):
    if count == 1:
        return temp[0]
    space = int(math.ceil((max_len - float(sum([len(x) for x in temp]))) / (count - 1)))
    i = 0
    res = ''
    max_len = max_len - len(temp[-1])
    for i in range(len(temp) - 1):
        res += temp[i]
        space = min(space, max_len - len(res))
        res += ' ' * space
    res += temp[-1]
    return res


def text_justification(words, max_len):
    res = []
    temp = []
    length = 0
    count = 0
    for x in words:
        if len(x) + length > max_len:
            res.append(justify(temp, count, max_len))
            temp = [x]
            length = len(x) + 1
            count = 1
        else:
            temp.append(x)
            count += 1
            length += len(x) + 1
    res.append(justify(temp, count, max_len))
    return res


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    print text_justification(words, 20)
