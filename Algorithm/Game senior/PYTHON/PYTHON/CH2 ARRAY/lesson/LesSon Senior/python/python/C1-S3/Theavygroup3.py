# Exercise 01
def numberOfUpperCase(word):
    numberUpperCase = 0
    for i in range(len(word)):
        if (word[i] == word[i].upper()) and (word[i] != " "):
            numberUpperCase += 1
    return numberUpperCase 

text = input("Word:")
print(numberOfUpperCase(text))

# Exercise 02
def getComment(grade):
    message = "Bad"
    if grade > 10:
        message = "Good"
    return message

print(getComment(12) + getComment (8))

# Exercise 03
def getPrice(fruitName):
    result = 0
    if fruitName == "banana":
        result = 2
    elif fruitName == "apple":
        result = 5
    elif fruitName == "orange":
        result = 1
    return result

print("banana price is: " + str(getPrice("banana")) + " dollars")
print("orange price is: " + str(getPrice("orange")) + " dollars")

# Exercise 04
def getAbsolute(number):
    if number < 0:
        return -1 * number
    else:
        return number

print(getAbsolute(5) + 10)

# Exercise 05
def max(number1, number2):
    result = 0
    if number1 > number2:
        result = number1
    else:
        result = number2
    return result

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
print("Maximum is " + str(max(num1, num2)))

# Exercise 06
def reverseString(word):
    result = ""
    lastIndex = len(word) - 1
    for i in range(len(word)):
        result += word[lastIndex - i]
    return result

text = input()
print(reverseString(text))