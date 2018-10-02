import math


def getMoney():

    money = 20000
    add_cost = None

    for i in map(int, input().rstrip().split(' ')):
        #남은 돈 체크
        if money < 0:
            money += add_cost
            break

        if 4 <= i <= 178:
            if i < 41:
                money -= 720
            else:
                add = i - 40
                add_cost = math.ceil(add/8) * 80
                money -= 720 + add_cost
        else:
            break

    return money


if __name__ == '__main__':
    res = getMoney()
    print(res)
