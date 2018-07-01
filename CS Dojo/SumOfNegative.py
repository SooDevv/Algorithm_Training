list = [7, 5, 4, 4, 3, 1, -2, 1, -3, -5, -7]

total = 0
## solution 1
# for i in range(len(list)):
#     if list[i] < 0:
#         total += list[i]
#
# print(total)  #-17



## solution 2
i = 0
while i < len(list):
    if list[i] < 0:
        total += list[i]
    i += 1
print(total)