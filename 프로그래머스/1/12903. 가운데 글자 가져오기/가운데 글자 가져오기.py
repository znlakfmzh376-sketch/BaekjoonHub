def solution(s):
    answer = ''
    x= len(s)
    y=int(x/2)
    if x %2==0:
        answer += s[y-1:y+1]
    else:
        answer += s[y] 
    return answer