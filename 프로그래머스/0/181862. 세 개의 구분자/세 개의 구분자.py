def solution(myStr):
    answer = []
    alphabet=''
    myStr=myStr.replace('a',' ')
    myStr=myStr.replace('b',' ')
    myStr=myStr.replace('c',' ')
    for i in myStr:
        if i !=' ':
            alphabet += i
        else:
            if len(alphabet)>0:
                answer.append(alphabet)
                alphabet=''
            else:
                pass
    if len(alphabet)>0:
                answer.append(alphabet)      
    if len(answer)==0:
        answer.append("EMPTY")
    
    return answer