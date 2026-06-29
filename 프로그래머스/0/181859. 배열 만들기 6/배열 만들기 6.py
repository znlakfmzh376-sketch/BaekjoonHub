def solution(arr):
    answer = []
    stk = []
    idx=0
    while idx != len(arr):
        if len(stk)==0:
            stk.append(arr[idx])
            idx +=1
        elif (len(stk)>0)&(stk[-1]==arr[idx]):
            stk.pop()
            idx +=1
        elif (len(stk)>0)&(stk[-1] != arr[idx]):
            stk.append(arr[idx])
            idx +=1
    if len(stk)==0:
        stk.append(-1)
    answer=stk        
    return answer