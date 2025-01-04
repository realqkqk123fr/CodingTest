import sys
input = sys.stdin.readline

a = [0]*4
b = [0]*2
for i in range(4):
    a[i] = int(input())
for i in range(2):
    b[i] = int(input())

a.sort()
total = a[3] + a[2] + a[1] + max(b)
print(total)