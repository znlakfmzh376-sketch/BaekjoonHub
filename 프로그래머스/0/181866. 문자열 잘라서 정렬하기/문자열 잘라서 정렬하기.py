def solution(myString):
    answer = []
    arr=''
    for i in myString:
        if i=='x':
            if arr=='':
                pass
            else:
                answer.append(arr)
                arr=''
        else:
            arr += i
    if len(arr)>0:
        answer.append(arr)
    answer.sort()    
    return answer