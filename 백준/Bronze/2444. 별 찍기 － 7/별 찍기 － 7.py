n = int(input())

for i in range(2*n-1):
    if (i > n - 1):
        print(" "*(i%n + 1) + "*"*(2*n - (2*(i%n + 1) + 1)))
    else:
        print(" "*(n-i-1) + "*"*(2*i+1))