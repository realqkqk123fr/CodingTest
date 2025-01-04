import sys
input = sys.stdin.readline

total = 0
for _ in range(4):
    a = int(input())
    total += a

print(total // 60)
print(total % 60)
