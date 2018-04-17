def StrStr(haystack, needle):
    length = len(needle)
    for i in range(0, len(haystack) - length + 1):
        if haystack[i: i + length] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "lla"
    print StrStr(haystack, needle)
