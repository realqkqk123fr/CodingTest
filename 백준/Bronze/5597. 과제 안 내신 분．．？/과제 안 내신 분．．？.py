a = []
b = []

for i in range(1, 31):
    a.append(i)

for i in range(28):
    n = int(input())
    b.append(n)

for num in a:
    if num not in b:
        print(num)