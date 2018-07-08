try:
    print('파일 이름을 입력하시오:', end='')
    filename = input()
    with open(filename) as f:
        print(f.read())

except FileNotFoundError:
    print('파일이 존재하지 않아 읽을 수 없습니다')