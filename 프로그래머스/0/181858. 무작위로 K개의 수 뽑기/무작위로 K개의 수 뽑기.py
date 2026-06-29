def solution(arr, k):
    answer = []
    for i in arr:
        if len(answer)==0:
            answer.append(i)
        elif i not in answer:
            answer.append(i)
        if len(answer)==k:
            break
    while len(answer)<k:
        answer.append(-1)
        
    return answer