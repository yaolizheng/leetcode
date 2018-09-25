class iter(object):

    def next(self):
        pass

    def hasNext(self):
        pass


class peek_iter(iter):

    def __init__(self):
        self.flag = False
        self.value = None

    def peek(self):
        self.value = self.next()
        self.flag = True
        return self.value

    def next(self):
        if self.flag:
            res = self.value
            self.flag = False
        else:
            res = self.next()
        return res

    def hasNext(self):
        res = self.hasNext()
        if not res:
            return (self.flag is True)
        return res


if __name__ == '__main__':
    pass
