class interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '[%s:%s]' % (self.start, self.end)


def merge_interval(l):
    l.sort(key=lambda x: x.start)
    res = []
    res.append(l[0])
    for i in range(1, len(l)):
        current = l[i]
        last = res.pop()
        if current.start > last.end:
            res.append(last)
            res.append(current)
        else:
            res.append(interval(last.start, max(last.end, current.end)))
    return res

if __name__ == '__main__':
    intervals = []
    intervals.append(interval(1, 4))
    intervals.append(interval(4, 5))
    # intervals.append(interval(1, 3))
    # intervals.append(interval(2, 6))
    # intervals.append(interval(8, 10))
    # intervals.append(interval(15, 18))
    print merge_interval(intervals)
