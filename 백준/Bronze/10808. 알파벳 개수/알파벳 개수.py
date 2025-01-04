a = input()
b = [0]*26

for i in a:
    b[ord(i) - ord('a')] += 1
print(*b)