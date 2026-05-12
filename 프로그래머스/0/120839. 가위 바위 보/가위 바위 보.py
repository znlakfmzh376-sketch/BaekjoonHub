def solution(rsp):
    answer = ''
    arr=[]
    for i in range(len(rsp)):
        if rsp[i]=='2':
            arr.append('0')
        elif rsp[i] == '0':
            arr.append('5')
        else:
            arr.append('2')
    answer=''.join(arr)
        
    return answer