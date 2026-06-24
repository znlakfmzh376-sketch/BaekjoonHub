import math as m
def solution(progresses, speeds):
    answer = []
    arr = []
    count =0
   
    for i,j in zip(progresses,speeds):
        process = 100 -i
        days = m.ceil(process / j)
        arr.append(days)
    stand =arr[0]
    for day in arr:
        if day<=stand:
            count +=1
        else:
            answer.append(count)
            stand =day
            count = 1
    answer.append(count)        
    return answer