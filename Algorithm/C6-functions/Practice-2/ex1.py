def nbUppercases(str):
    result=0
    for i in range(len(str)):
        if str[i]==str[i].upper():
            result+=1
    return result
str=input()
print(nbUppercases(str))