def solution(n):
    answer = 0
    result = 1
    while result <= n:
        answer +=1
        result *=answer
    return answer-1