def majority(l):
    count = {}
    for x in l:
        if x not in count:
            count[x] = 0
        count[x] += 1
        if count[x] > (len(l) / 2):
            return x


def majority2(l):
    candidate = None
    count = 0
    for x in l:
        if count == 0:
            candidate = x
        count = count + 1 if x == candidate else count - 1
    return candidate


if __name__ == '__main__':
    l = [2, 2, 1, 1, 1, 2, 2]
    print majority2(l)
