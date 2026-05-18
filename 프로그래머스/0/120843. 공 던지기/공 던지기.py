def solution(numbers, k):
    answer = 1
    for i in range(1,k,1):
        answer +=2
    answer = answer % len(numbers)
    if answer ==0:
        answer = len(numbers)
    return answer