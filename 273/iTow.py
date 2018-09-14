def iTow(n):
    res = convert(n % 1000)
    thousand = [" thousand ", " million ", " billion "]
    for i in thousand:
        n = n / 1000
        temp = convert(n % 1000)
        if temp != '':
            res = temp + i + res
        else:
            break
    return res


def convert(n):
    if n == 0:
        return ''
    one = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    ten = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    h = (one[n / 100] + ' hundred') if n / 100 > 0 else ''
    t = n % 100
    if t == 0:
        return h if h != '' else ''
    elif t < 20:
        t = one[t]
    else:
        t = ten[t / 10 % 10]
    return h + ' and ' + t if h != '' else t


if __name__ == '__main__':
    n = 1001140
    print iTow(n)
