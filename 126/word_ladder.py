def is_valid(word1, word2):
    if len(word1) != len(word2):
        return False
    miss = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            miss += 1
            if miss > 1:
                return False
    return True


def helper(start, end, temp, wordlist):
    if start == end:
        if len(helper.res) == 0 or len(temp) < len(helper.res):
            helper.res = temp
        return
    for word in wordlist:
        if word in temp:
            continue
        if is_valid(word, start):
            helper(word, end, temp + [word], wordlist)


def word_ladder(start, end, wordlist):
    helper.res = []
    helper(start, end, [start], wordlist)
    return helper.res


if __name__ == '__main__':
    start = 'hit'
    end = 'cog'
    wordlist = ["hot", "dot", "dog", "lot", "log"]
    print word_ladder(start, end, wordlist)
