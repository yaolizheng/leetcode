def ga(word):
    res = []
    for i in range(len(word) ** 2):
        count = 0
        out = ""
        for j in range(len(word)):
            if i & 1 == 1:
                count += 1
                if j == len(word) - 1:
                    out += str(count)
            else:
                if count != 0:
                    out += str(count)
                    count = 0
                out += word[j]
            i = i >> 1
        res.append(out)
    return res


if __name__ == '__main__':
    word = 'word'
    print ga(word)
