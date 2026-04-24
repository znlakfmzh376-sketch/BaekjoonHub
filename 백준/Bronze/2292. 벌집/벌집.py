import sys
input = sys.stdin.readline

N = int(input())

count = 1   
layer = 1   
while N > count:
    count += 6 * (layer)
    layer += 1

print(layer)