N, M = map(int, input().split())
a = []
b = []

for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    b.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        a[i][j] = a[i][j] + b[i][j]
        print(a[i][j], end = " ")
    print()