n = int(input())
sum = 0

array = list(map(int, input()))
for i in range(n):
    sum += array[i]
    
print(sum)