import sys


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


def helper(start, end, l, wordlist):
    if start == end:
        helper.res = min(helper.res, l)
        return
    for word in wordlist:
        if is_valid(word, start):
            wordlist.remove(word)
            helper(word, end, l + 1, wordlist)
            wordlist.append(word)


def word_ladder(start, end, wordlist):
    helper.res = sys.maxint
    helper(start, end, 1, wordlist)
    return 0 if helper.res == sys.maxint else helper.res


if __name__ == '__main__':
    start = 'hit'
    end = 'cog'
    wordlist = ["hot", "dot", "dog", "lot", "log"]
    print word_ladder(start, end, wordlist)
