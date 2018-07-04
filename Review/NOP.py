s = input('* press enter to quit system')

P = []
O = []
N = []

while 1:
    if s == '':
        break
    elif int(s) < 0:
        N.append(s)
    elif int(s) == 0: # s = 0 : binding , s == 0 : check number
        O.append(s)
    else:
        P.append(s)
    s = input()

output = N + O + P
print(output)