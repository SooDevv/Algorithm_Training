while True:
    print('숫자를 입력해주세요 :', end="")
    n = input()

    if not n.isnumeric():
        print(n, '은 숫자가 아닙니다. 다시 입력해주세요')
        continue

    n = int(n)

    if n == 0:
        print('0으로 나눌 수 없습니다. 다시입력해주세요')
        continue

    break

print(1/ n)
