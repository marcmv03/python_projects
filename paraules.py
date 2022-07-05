x = input()
dict = {}
while x != '0' :
    if x in dict :
        dict[x] = dict[x] +1
    else :
        dict[x] = 1

    x = input()

print(dict)
