def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(b,a)+1,1):
        answer += i
    return answer