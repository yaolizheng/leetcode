def valid_num(s):
    s = s.strip()
    try:
        if isinstance(float(s), float) or isinstance(int(s), int):
            return True
    except:
        return False
    return False


if __name__ == '__main__':
    print valid_num("0")
    print valid_num(" 0.1")
    print valid_num("2e10")
