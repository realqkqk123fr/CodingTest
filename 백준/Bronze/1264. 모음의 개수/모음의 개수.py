import sys
input = sys.stdin.readline

while True:
    l = input().strip()
    count = 0
    if l == "#":
        break
    
    r = l.lower()
    count = r.count('a') + r.count('e') + r.count('i') + r.count('o') + r.count('u')
    
    print(count)