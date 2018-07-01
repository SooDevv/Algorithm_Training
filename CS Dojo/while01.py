## list = [5, 4, 3, 1, -1, -2, -4]
## while 문은 list 의 index(4) 에서 조건문인 list[i] > 0 (break point) 에 의해 loop를 빠져나가게 된다.

## list2 = [5, 4, 3, 1]
## while의 조건문인 list[i] > 0 과 'i += 1' 에 의해 loop를 빠져나가지 못하고 Index error 가 났다
## 해결 방법은 조건문을 추가해 주는 것

list = [5, 4, 3, 1]
total = 0

i = 0
while i < len(list) and list[i] > 0:
    total += list[i]
    i += 1

print(total)