def solution(x, n):
    answer = []
    for i in range(0,n,1):
        answer.append(x + (x*i))   
    return answer