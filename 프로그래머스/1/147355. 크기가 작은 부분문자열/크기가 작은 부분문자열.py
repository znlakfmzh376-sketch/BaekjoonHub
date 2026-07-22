def solution(t, p):
    answer = 0
    arr =[]
    for i in range(len(t)-len(p)+1):
        arr.append(t[i:len(p)+i])
    for j in arr:
        if int(p)>=int(j):
            answer+=1
    return answer