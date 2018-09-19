# [119, 97674223, 1195524421]
# 전화번호부에서 임의의 한 번호가 다른 번호들에 접두어라면 false 출력, 아니면 true
def solution(phone_book):

    phone_book.sort()

    pre = phone_book[0]
    answer = True

    for i in phone_book[1:]:
        if pre in i[:len(pre)]:
            answer = False

    return answer


if __name__ == '__main__':

    result = solution(["119", "97674223", "1195524421"])
    print(result)