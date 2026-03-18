import sys
input = sys.stdin.readline

month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x,y=map(int,input().split())
days=0
for i in range(0,x-1,1):
    days +=month[i]

days +=y
result= days%7
print(week[result-1])    

