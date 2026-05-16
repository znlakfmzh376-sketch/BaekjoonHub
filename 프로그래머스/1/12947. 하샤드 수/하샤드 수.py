def solution(x):
    answer = True
    sum_x=0
    str_x=str(x)
    for i in str_x:
        sum_x += int(i)
    if x % sum_x==0:
        answer =bool(1)
    else:
        answer =bool(0)
        
    return answer