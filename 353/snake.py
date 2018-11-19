class Snake:

    def __init__(self, w, h, food):
        self.w = w
        self.h = h
        self.food = food
        self.pos = []
        self.pos.append([0, 0])
        self.score = 0

    def move(self, d):
        head = [self.pos[0][0], self.pos[0][1]]
        tail = [self.pos[-1][0], self.pos[-1][1]]
        self.pos.pop()
        if d == 'U':
            head[0] -= 1
        elif d == 'D':
            head[0] += 1
        elif d == 'L':
            head[1] -= 1
        else:
            head[1] += 1
        if head in self.pos or head[0] < 0 or head[0] >= h or head[1] < 0 or head[1] >= w:
            return -1
        self.pos.insert(0, head)
        if food and head == food[0]:
            del food[0]
            self.pos.append(tail)
            self.score += 1
        return self.score


if __name__ == '__main__':
    w = 3
    h = 2
    food = [[1, 2], [0, 1]]
    test = Snake(w, h, food)
    print test.move('R')
    print test.move('D')
    print test.move('R')
    print test.move('U')
    print test.move('L')
    print test.move('U')
