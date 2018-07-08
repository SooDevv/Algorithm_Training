def get(key, dataset):
    '''key 를 인덱싱하여 dataset에서 값을 찾아내고
    error 가 난다면(즉 key 값 혹은 그에 해당하는 value 가 없다면 none을 반환'''


    try:
        result = dataset[key]
    except (IndexError, KeyError):
        return None
    else:
        return result

# tuple (1,2,3) 에서 인덱스가 1인값 가져오기
print(get(1,(1,2,3,)))

# list [4,5,6] 에서 인덱스가 3인값 가져오기 ==> error 가 나겠죠?
print(get(3, [4,5,6]))

# dict {'name':'김수정', 'age':26} 에서 age 가져오기
print(get('age', {'name':'김수정', 'age':26}))

# dict {'name':'김수정', 'age':26} 에서 personality 가져오기 =+> error 가 나겠죠??4
print(get('personality', {'name':'김수정', 'age':26}))


