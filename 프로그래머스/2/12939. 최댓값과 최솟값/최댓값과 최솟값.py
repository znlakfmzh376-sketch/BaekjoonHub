def solution(s):
    answer = ''
    arr= list(s.split(" "))
    arr2=[]
    for i in arr:
        arr2.append(int(i))
    a = min(arr2)
    b = max(arr2)
    answer= str(a)+" "+str(b)
    return answer