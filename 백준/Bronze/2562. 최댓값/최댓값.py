b = []

for i in range(9):
    n = int(input())
    b.append(n)

maX = max(b)
maxIndex = b.index(maX) + 1

print(maX)
print(maxIndex)