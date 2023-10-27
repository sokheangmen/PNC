def retagele(number):
    result=""
    for i in range(number):
        for j in range(number):
            result+="X"
        result+="\n"
    return result
number=retagele(3)
print(number)
