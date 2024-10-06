N, M = map(int, input().split())
basket = [0]*N

for i in  range(M):
    x, y, z = map(int, input().split())
    for j in range(x - 1, y):
            basket[j] = z

for i in range (N):
      print(basket[i], end=" ")