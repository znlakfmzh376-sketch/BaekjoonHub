def solution(balls, share):
    answer = 1
    a = balls - share 
    for i in range(balls,share,-1):
        answer *= i
    for i in range(1,a+1):
        answer //= i
    return answer