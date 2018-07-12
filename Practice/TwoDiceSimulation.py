#simulate = 1000
#function , no parameter ,return total
#simulated percent = sum of two dice / 1000
#expected percent =
import random

def roll():
    i = 0
    while i < 3 :
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)

        print(dice1, dice2)

        # 두 dice 의 합
        total = dice1 + dice2
        print(total)
        dice_dict = {}

        #dice_dict key 값에 total 있으면 key 추가하고 +1
        #dice_dict 에 있다면 해당 key 의 value 값 +1
        if total in dice_dict.keys():
            dice_dict[total] += 1
            print('이미 key가 있네용')
        else:
            dice_dict[total] = 1
            print('키가 없네용 추가할꼐용')
        i += 1

    return dice_dict





roll()