import sys


def buy(n):
    pre_buy = 0
    buy = -sys.maxint + 1
    pre_sell = 0
    sell = 0
    for x in n:
        pre_buy = buy
        buy = max(pre_sell - x, pre_buy)
        pre_sell = sell
        sell = max(pre_buy + x, pre_sell)
    return sell


if __name__ == '__main__':
    n = [1, 2, 3, 0, 2]
    print buy(n)
