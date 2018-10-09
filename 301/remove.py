def is_valid_paran(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def remove_invalid_paran(s):
    visited = []
    res = []
    queue = []
    queue.append(s)
    level = False
    while len(queue) > 0:
        x = queue.pop(0)
        if is_valid_paran(x):
            res.append(x)
            level = True
        if level:
            continue
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                continue
            temp = s[:i] + s[i + 1:]
            if temp not in visited:
                queue.append(temp)
                visited.append(temp)
    return res


if __name__ == '__main__':
    s = '()())()'
    print remove_invalid_paran(s)
