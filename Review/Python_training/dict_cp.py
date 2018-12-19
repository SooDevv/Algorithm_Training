# list1 : 1 -10, range로 담기
# list2 : 서수담기(one~ten)
# for문을 이용하여 딕셔너리로 만들기

list1 = [i for i in range(1, 11)]
list2 = ['one','two','three', 'four','five','six','seven','eight','nine','ten']

dic_for = {i:j for i, j in zip(list1, list2)}
print(dic_for)