def solution(i, j, k):
    answer = 0
    b=str(k)
    for l in range(i,j+1,1):
        a=str(l)
        if b in a:
            answer+=a.count(b)
    return answer