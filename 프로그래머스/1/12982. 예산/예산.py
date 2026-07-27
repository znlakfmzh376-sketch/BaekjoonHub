def solution(d, budget):
    answer = 0
    total=0
    d=sorted(d)
    for i in range(len(d)):
        total += d[i]
        if total>budget:
            break
        else:
            answer += 1
            
    return answer