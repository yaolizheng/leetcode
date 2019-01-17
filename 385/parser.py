class NestedInteger:

    def __init__(self, value=None):
        self.value = list()
        if value:
            self.value.append(value)

    def add(self, value):
        self.value.append(value)


def deserialize(s):
    if len(s) == 0:
        return NestedInteger()
    if s[0] != '[':
        return NestedInteger(s)
    if len(s) <= 2:
        return NestedInteger()
    count = 0
    start = 1
    res = NestedInteger()
    for i in range(1, len(s)):
        if count == 0 and (s[i] == ',' or i == len(s) - 1):
            res.add(deserialize(s[start:i]))
            start = i + 1
        elif s[i] == '[':
            count += 1
        elif s[i] == ']':
            count -= 1
    return res


def print_nested(i):
    for v in i.value:
        if isinstance(v, NestedInteger):
            print_nested(v)
        else:
            print v


if __name__ == '__main__':
    s = "[123,[456,[789]]]"
    print_nested(deserialize(s))
