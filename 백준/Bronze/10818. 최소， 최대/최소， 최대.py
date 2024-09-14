n = int(input())
a = list(map(int, input().split()))
maX = a[0]
miN = a[0]

for i in range(n):
    if maX < a[i]:
        maX = a[i]
    
    if miN > a[i]:
        miN = a[i]

print(miN, maX)