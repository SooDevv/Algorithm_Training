# s = input('* press enter to quit system')

P = []
O = []
N = []

while 1:
    s = input()
    if s == '':
        break

    try:
        num = int(s)
    except:
        continue

    if num < 0:
        N.append(s)
    elif num == 0: # s = 0 : binding , s == 0 : check number
        O.append(s)
    else:
        P.append(s)

output = N + O + P
print(output)

