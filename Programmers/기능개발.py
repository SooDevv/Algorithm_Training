# 역시 python ..
# 우아하다 못해 감동을 준다

from math import ceil


def solution(progresses, speeds):
    Q = []

    for p,s in zip(progresses, speeds):
        job = ceil((100-p)//s)

        if len(Q) == 0 or Q[-1][0] < job:
            Q.append([job, 1])
        else:
            Q[-1][1] += 1

    return [q[1] for q in Q]