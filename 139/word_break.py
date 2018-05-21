def word_break(s, d):
    n = len(s)
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        if dp[i] is False and s[:i] in d:
            dp[i] = True
        if dp[i]:
            if i == n:
                return True
            for j in range(i + 1, n + 1):
                if dp[j] is False and s[i: j] in d:
                    dp[j] = True
                if j == n and dp[j] is True:
                    return True


if __name__ == '__main__':
    s = 'applepen'
    d = ["apple", "pen"]
    print word_break(s, d)
