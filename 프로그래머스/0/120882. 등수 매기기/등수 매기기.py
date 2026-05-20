def solution(score):
    answer = []
    arr=[]
    arr2=[]
    for i,j in score:
        mean = (i+j)/2
        arr.append(mean)
    arr2=sorted(arr,reverse=True)
    for i in arr:
        answer.append(arr2.index(i)+1)
    return answer