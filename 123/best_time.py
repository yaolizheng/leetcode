def best_time(l):
    res = 0
    current_min = l[0]
    max_profit = 0
    profit = []
    res = 0
    for x in l:
        current_min = min(x, current_min)
        max_profit = max(max_profit, x - current_min)
        profit.append(max_profit)
    current_max = l[-1]
    max_profit = 0
    for i in range(len(l) - 1, -1, -1):
        current_max = max(l[i], current_max)
        max_profit = max(max_profit, current_max - l[i])
        res = max(res, max_profit + profit[i])
    return res


if __name__ == '__main__':
    l = [3, 3, 5, 0, 0, 3, 1, 4]
    print best_time(l)
