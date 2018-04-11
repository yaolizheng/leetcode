def palindrome_num(num):
    reverse = 0
    while num > reverse:
        reverse = reverse * 10 + num % 10
        num = num / 10
        if reverse == num or num / 10 == reverse:
            return True
    return False


if __name__ == '__main__':
    num = 1233291
    print palindrome_num(num)
