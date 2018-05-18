import sys


def gas_cost(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total = 0
    min = sys.maxint
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < min:
            min = total
            start = (i + 1) % len(gas)
    return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print gas_cost(gas, cost)
