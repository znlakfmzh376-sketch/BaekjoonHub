def solution(order):
    answer = 0
    for i in order:
        if i.count('americano')>0:
            answer += 4500
        elif i.count('cafelatte') >0:
            answer += 5000
        else:
            answer += 4500
    return answer