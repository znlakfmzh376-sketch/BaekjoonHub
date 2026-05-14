def solution(before, after):
    answer = 0
    a=sorted(before)
    b=sorted(after)
    if a==b:
        answer=1
    else:
        answer=0
    return answer