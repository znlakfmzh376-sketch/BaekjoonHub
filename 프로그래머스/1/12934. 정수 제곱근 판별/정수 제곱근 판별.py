def solution(n):
    answer = 0
    x = int(n**0.5)
    if x*x==n:
        answer = (x+1)**2
    else:
        answer= -1
    return answer