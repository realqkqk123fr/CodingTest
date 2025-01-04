while True:
    a = list(input().split())
    if (a[0] == "#"):
        break

    if int(a[1]) > 17 or int(a[2]) >= 80:
        print(a[0], "Senior")
    else:
        print(a[0], "Junior")