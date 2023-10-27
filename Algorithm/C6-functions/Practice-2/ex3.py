def getAbsolute(number):
    if number < 0:
        return -1 * number
    else:
        return str(number)
number=int(input("Enter your number"))
print(getAbsolute(number))