def solution(names):
    answer = []
    for i in range(len(names)):
        if i ==0:
            answer.append(names[i])
        elif i % 5 ==0:
            answer.append(names[i])
            
    return answer