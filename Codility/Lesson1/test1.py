n = int(input())

for i in range(1, n+1): # n 줄
    for j in range(i): # Line1 --> * 한개, line2 --> * * (별 두개)
        print('* ', end='')
    print()