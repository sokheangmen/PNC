# ex 1
def removeMinses(word):
    newtext = ""
    for i in range(len(word)):
        if word[i] != "-":
            newtext += word[i]
    return newtext

continuePrograme = True
while continuePrograme:
    text = input("Enter a word:")
    result = removeMinses(text)
    print(result)
    check_Answer = input("Do you want to continue (Y/N)?:")
    if check_Answer != "Y":
        continuePrograme = False
    continuePrograme = check_Answer == "Y"
    
# ex 2
def sum(number1, number2):
    return number1 + number2

integer1 = int(input("Number 1: "))
integer2 = int(input("Number 2: "))
print("The sum is:"+ str(sum(integer1,integer2)))


# ex 3
def sum(number1,number2):
    return number1 + number2

values = int(input("Number of values: "))
sumOfNumber = 0
for i in range(values):
    value = int(input("Value" + str(i+1) + ":"))
    sumOfNumber = sum(sumOfNumber,value)
print(sumOfNumber)


# ex 4
def sumFromTo(start, end):
    sumofnumber = 0
    for i in range (start, end+1):
        sumofnumber += i
    return sumofnumber
    
startvalue = int(input("Start value : "))
endvalue = int(input("End value : "))
print(sumFromTo(startvalue,endvalue))