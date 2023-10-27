# Activity 02
def ExchangeDollarToKhmer(number):
    TheResultExchange = number * 4000
    return TheResultExchange

# print(ExchangeDollarToKhmer(3))

# Activity 03
def rectangle(number):
    rectangleofX = ""
    for i in range(number):
        rectangleofX += "X"*number + "\n"
    return rectangleofX

# print(rectangle(5))


# Activity 04
def countLetterX(String):
    numberofletterX = 0
    for i in range(len(String)):
        if String[i] == "X":
            numberofletterX += 1
    return numberofletterX

# print(countLetterX("AADDXXXDD"))