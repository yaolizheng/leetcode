def substring_with_words(s, words):
    length = len(words[0])
    include = []
    i = j = 0
    res = []
    while j < len(s):
        word = s[j: j + length]
        print include
        if word in words and word not in include:
            include.append(word)
            if len(include) == len(words):
                res.append(i)
                while len(include) == len(words):
                    pre_word = s[i: i + length]
                    if pre_word in words:
                        include.remove(pre_word)
                    i += length
        else:
            include = []
            i = j + length
        j += length
    return res


if __name__ == '__main__':
    s = 'barfoothefoobarman'
    words = ['foo', 'bar']
    print substring_with_words(s, words)
