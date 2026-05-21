def solution(common):
    answer = 0
    d1= common[1] - common[0]
    d2= common[2] - common[1]
    if d1 == d2:
        answer = common[len(common)-1] + d1
    else:
        r = common[1] // common[0]
        answer = common[len(common)-1] * r
    return answer