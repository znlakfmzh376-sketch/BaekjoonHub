def solution(rank, attendance):
    answer = 0
    temp=[]
    temp2=[]
    result=''
    for i in range(len(rank)):
        if attendance[i]==False:
            pass
        else:
            temp.append(rank[i])
    temp=sorted(temp)
    for i in temp:
        if i in rank:
            temp2.append(rank.index(i))
        else:
            pass
    answer= temp2[0]*10000 + 100*temp2[1] + temp2[2]        
            
    return answer