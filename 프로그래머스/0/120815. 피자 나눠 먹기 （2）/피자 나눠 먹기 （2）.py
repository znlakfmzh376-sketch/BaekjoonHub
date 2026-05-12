def solution(n):
    answer = 0
    i=0
    while True:
        i +=1
        if (6*i) %n==0:
            answer=i
            break
        
    return answer