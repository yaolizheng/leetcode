class interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '[%s:%s]' % (self.start, self.end)


def insert_interval(l, target):
    res = []
    for i in range(len(l)):
        current = l[i]
        if current.start > target.end:
            res.append(target)
            res += l[i:]
            return res
        elif current.end < target.start:
            res.append(current)
        else:
            target = interval(min(current.start, target.start), max(current.end, target.end))
    return res

if __name__ == '__main__':
    intervals = []
    intervals.append(interval(1, 2))
    intervals.append(interval(3, 5))
    intervals.append(interval(6, 7))
    intervals.append(interval(8, 10))
    intervals.append(interval(12, 16))
    target = interval(4, 8)
    # intervals.append(interval(1, 3))
    # intervals.append(interval(2, 6))
    # intervals.append(interval(8, 10))
    # intervals.append(interval(15, 18))
    print insert_interval(intervals, target)
