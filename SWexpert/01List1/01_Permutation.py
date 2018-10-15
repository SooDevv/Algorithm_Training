# Baby-gin game : 연속된 숫자 3개(run), 같은 숫자 3개(triplete)
# brute-force 방식은 모든 순열 생성 후, 앞 뒤 세개씩 확인

# ex. {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3!=i1 and i3!=i2:
                    print(i1, i2, i3)
