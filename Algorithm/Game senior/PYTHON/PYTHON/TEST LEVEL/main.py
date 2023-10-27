# array = [4,5,8,7]
# result = 0
# value = 0

# for arr in array:
#     if arr%2 == 1:
#         value += arr
#         result += 1
# print (round(value / result))


# EX2


dict = {"him":21,"Rady":25,"Ronan":30,"Clement":22,"Edoure":22}
result = 0
count = 0
if dict == "":
    print ("No teaccher here")
    else:
        for key in dict:
            result += dict[key]
            count += 1
        print (result / count)
