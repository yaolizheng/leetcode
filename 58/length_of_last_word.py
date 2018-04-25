def length_of_last_word(w):
    l = 0
    for i in range(len(w) - 1, -1, -1):
        if w[i] == ' ':
            return l
        l += 1
    return 0


if __name__ == '__main__':
    w = 'Hello World'
    print length_of_last_word(w)
