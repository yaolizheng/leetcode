class Log():

    def __init__(self):
        self.mapping = dict()
        self.timeout = 10

    def shouldPrintMessage(self, ts, message):
        if message not in self.mapping:
            self.mapping[message] = ts
            return True
        if self.mapping[message] + self.timeout <= ts:
            return True
        return False


if __name__ == '__main__':
    log = Log()
    print log.shouldPrintMessage(1, "foo")
    print log.shouldPrintMessage(2, "bar")
    print log.shouldPrintMessage(3, "foo")
    print log.shouldPrintMessage(8, "bar")
    print log.shouldPrintMessage(10, "foo")
    print log.shouldPrintMessage(11, "foo")
