def verify_preorder(l):
    count = 0
    for i in range(len(l) - 1):
        if l[i] == '#':
            if count == 0:
                return False
            count -= 1
        else:
            count += 1
    return count == 0 and l[-1] == '#'


if __name__ == '__main__':
    l = [9, 3, 4, '#', '#', 1, '#', '#', 2, '#', 6, '#', '#']
    print verify_preorder(l)
