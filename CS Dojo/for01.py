a = list(range(1, 1000))

total = 0
for i in a:
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

## another solution
# for i in a:
#     if i % 3 ==0:
#         total += i
#     elif i % 5 == 0:
#         total += i
# print(total)