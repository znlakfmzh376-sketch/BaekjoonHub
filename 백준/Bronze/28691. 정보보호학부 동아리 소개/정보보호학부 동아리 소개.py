import sys
input = sys.stdin.readline

isi = {"M":"MatKor", "W":"WiCys","C":"CyKor", "A":"AlKor","$":"$clear"}
a=input().strip()
print(isi[a])