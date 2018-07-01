## if 문이 break 면, total = 9
## if 문이 continue 이면, total = 10

list = [5, 4, -1, 1, -1, -2, -4]

total = 0
for ele in list:
    if ele < 0:
        break
    total += ele

print(total)  #9

