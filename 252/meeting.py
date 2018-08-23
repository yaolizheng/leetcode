class meeting:

    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __repr__(self):
        return '[%s %s]' % (self.s, self.e)


def can_attand(meetings):
    meetings.sort(key=lambda x: x.s)
    for i in range(1, len(meetings)):
        if meetings[i].s < meetings[i - 1].e:
            return False
    return True


if __name__ == '__main__':
    meetings = [meeting(0, 30), meeting(5, 10), meeting(15, 20)]
    print can_attand(meetings)
