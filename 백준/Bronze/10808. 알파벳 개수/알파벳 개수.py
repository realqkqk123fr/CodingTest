a = list(input())
b = [0]*26

for i in range(len(a)):
    if a[i] == 'a':
        b[0] += 1
    elif a[i] == 'b':
        b[1] += 1
    elif a[i] == 'c':
        b[2] += 1
    elif a[i] == 'd':
        b[3] += 1
    elif a[i] == 'e':
        b[4] += 1
    elif a[i] == 'f':
        b[5] += 1
    elif a[i] == 'g':
        b[6] += 1
    elif a[i] == 'h':
        b[7]+= 1
    elif a[i] == 'i':
        b[8] += 1
    elif a[i] == 'j':
        b[9] += 1
    elif a[i] == 'k':
        b[10] += 1
    elif a[i] == 'l':
        b[11] += 1
    elif a[i] == 'm':
        b[12] += 1
    elif a[i] == 'n':
        b[13] += 1
    elif a[i] == 'o':
        b[14] += 1
    elif a[i] == 'p':
        b[15] += 1
    elif a[i] == 'q':
        b[16] += 1
    elif a[i] == 'r':
        b[17] += 1
    elif a[i] == 's':
        b[18] += 1
    elif a[i] == 't':
        b[19] += 1
    elif a[i] == 'u':
        b[20] += 1
    elif a[i] == 'v':
        b[21] += 1
    elif a[i] == 'w':
        b[22]+= 1
    elif a[i] == 'x':
        b[23] += 1
    elif a[i] == 'y':
        b[24] += 1
    else:
        b[25] += 1
print(*b)