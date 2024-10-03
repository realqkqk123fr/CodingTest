str = input()
str1 = ""

for i in range(len(str) - 1, -1, -1): 
    str1 = str1 + str[i]

if (str == str1): 
    print(1)
else:
    print(0)