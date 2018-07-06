# 멤버쉽 연산자 사용해 볼 것
# in, not in

# s = input()
#
# check = []
# while True:
#     if s in check:
#         break
#     print(s)
#     check.append(s)
#     s = input()

# sol2
word_list = []
while True:
    word = input()
    if word is '':
        break
    try:
        word_list.index(word) ##word 가 wordlist 에 없다면 ValueError 가 나서 exccept 문 호출
    except:
        word_list.append(word)

for i in word_list:
    print(i)
