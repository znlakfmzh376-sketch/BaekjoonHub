def solution(myString, pat):
    answer = 0
    myString=myString.replace('A','x')
    myString=myString.replace('B','y')
    myString=myString.replace('x','B')
    myString=myString.replace('y','A')
    if myString.count(pat)>0:
        answer=1
    else:
        answer=0
    return answer