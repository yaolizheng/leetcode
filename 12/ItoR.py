def ItoR(i):
    map = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
           ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']]
    return map[3][i / 1000] + map[2][i % 1000 / 100] + map[1][i % 100 / 10] + map[0][i % 10]


if __name__ == '__main__':
    i = 8
    print ItoR(i)
