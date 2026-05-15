def solution(myString):
    answer = ''
    arr = ['a','b','c','d','e','f','g','h','i','j','k']
    for i in arr:
        myString=myString.replace(i,'l')
    answer=myString
    return answer