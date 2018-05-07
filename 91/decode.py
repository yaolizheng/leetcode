def decode(s):
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0
    for i in range(2, len(s) + 1):
        a = dp[i - 1] if s[i - 1] != '0' else 0
        b = dp[i - 2] if 10 <= int(s[i - 2: i]) <= 26 else 0
        dp[i] = a + b
    return dp[len(s)]


if __name__ == '__main__':
    s = '226'
    print decode(s)
