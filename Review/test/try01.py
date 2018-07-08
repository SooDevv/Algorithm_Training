while True:
    try:
        print('0이 아닌 정수를 입력해주세요 ', end='')
        n = int(input())
        result = 1/n
        # print(1 / n)
        # break
    except ZeroDivisionError:
        print('0 으로는 나눌 수 없습니다!! 다시 입력해 주세요!!!')
    except ValueError:
        print('정수 입력하라니깐 왜 문자 입력하냐???')
    else:
        print(result)
        break
