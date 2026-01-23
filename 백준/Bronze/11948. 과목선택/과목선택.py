import sys
input = sys.stdin.readline

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
F=int(input())

x = [A,B,C,D]
x.sort()
if E>F:
    print(E+(sum(x)-x[0]))
elif E<F:
    print(F+(sum(x)-x[0]))
else:
    print(F+(sum(x)-x[0]))        