import sys
input = sys.stdin.readline

A_str, A_hp = map(int, input().split())
B_str, B_hp = map(int, input().split())

while True:
    A_hp -= B_str
    B_hp -= A_str

    if A_hp <= 0 and B_hp <= 0:
        print("DRAW")
        break
    elif A_hp <= 0:
        print("PLAYER B")
        break
    elif B_hp <= 0:
        print("PLAYER A")
        break
