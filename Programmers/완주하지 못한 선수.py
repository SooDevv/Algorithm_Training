from collections import Counter


def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    fail = p-c
    return list(fail.keys())


result =solution(["mislav", "mislav", "stanko","ana","hh"], ["mislav", "stanko","ana"])
print(result)