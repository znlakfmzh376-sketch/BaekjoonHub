def solution(sides):
    answer = 0
    a=min(sides)
    b=max(sides)
    c=sum(sides)
    d=b-(b-a)
    e=c-b-1

    return d+e