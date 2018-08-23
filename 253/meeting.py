import heapq


class meeting:

    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __repr__(self):
        return '[%s %s]' % (self.s, self.e)


def rooms(meetings):
    meetings.sort(key=lambda x: x.s)
    heap = list()
    heapq.heappush(heap, meetings[0].e)
    count = 1
    for i in range(1, len(meetings)):
        if meetings[i].s < heap[0]:
            count += 1
        else:
            heapq.heappop(heap)
        heapq.heappush(heap, meetings[i].e)
    return count


if __name__ == '__main__':
    meetings = [meeting(0, 30), meeting(5, 10), meeting(15, 20)]
    print rooms(meetings)
