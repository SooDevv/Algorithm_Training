from collections import Counter

def checkMagazine(magazine, note):

    mag_dict = Counter(magazine)
    note_dict = Counter(note)

    for k, v in note_dict.items():
        if k in mag_dict:
            if v > mag_dict[k]: # 대소 비교로 해야함
                return 'No'
        else:
            return 'No'
    return 'Yes'


# 다른이의 풀이방법ㅎ 크...
# Counter와 차집합을 이용!!
def ransom_note(magazine, rasom):
    return (Counter(rasom) - Counter(magazine)) == {}


if __name__ == '__main__':
    mn = input().split()
    magazine = list(input().split())
    note = list(input().split())
    res = ransom_note(magazine, note)
    print(res)