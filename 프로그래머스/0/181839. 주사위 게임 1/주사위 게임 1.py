def solution(a, b):
    if (a %2 !=0 ) and (b %2 !=0 ):
        answer = (a**2) + (b**2)
    elif   (a %2 !=0 ) or (b %2 !=0 ):
        answer = 2*(a+b)
        
    else:
        answer = abs(a-b)
    return answer
print(solution(3, 5))
print(solution(6, 1))
print(solution(2, 4))