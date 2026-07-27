def solution(n):
    answer = 0
    for start in range(1,n+1,1):
        total =0
        for end in range(start,n+1,1):
            total += end
            if total ==n:
                answer += 1
            elif total>n:
                break;
    return answer