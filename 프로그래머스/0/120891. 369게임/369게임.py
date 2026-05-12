def solution(order):
    answer = 0
    a=str(order)
    nums=['3','6','9']
    for i in a:
        if i in nums:
            answer +=1
    return answer