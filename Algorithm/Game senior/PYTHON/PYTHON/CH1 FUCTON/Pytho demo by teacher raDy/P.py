# arr=[1,2,5,5]
# result=0
# for i in range(len(arr)):
#      if arr[i]%2==1:
#         result+=arr[i]
# print(result)
    # print(arr[-(1 + i)])
    # print(str(i)+"-"+str(arr[i]))

# យកលេខធំ

# arr=[2,3,4,5,6,7,8,9,10,11,12]
# max=arr[0]
# for i in range(len(arr)):
#     if max < arr[i]:
#         max=arr[i]
# print(max)


# small number


# arr=[2,3,4,5,6,7,8,9,10,2,11,12]
# max=arr[0]
# for i in range(len(arr)):
#     if max > arr[i]:
#         max=arr[i]
# print(max)

# sumnumber

# arr=[2,3,4,5,5,7,8,5,10,2,11,12]
# max=0
# for i in range(len(arr)):
#     if arr[i]==5:
#         max+=1
# print(max)


# រកindex number5

# arr=[2,3,4,5,5,7,8,5,10,2,11,12]
# max=0
# iSFount=False
# for i in range(len(arr)):
#     if arr[i]==5 and not iSFount:
#         iSFount=True
#         max=i
# print(max)


# meet number5 stop process

# arr=[2,3,4,5,5,7,8,5,10,2,11,12]
# max=0
# i=0
# iSFount=True
# while i<len(arr) and iSFount:
#     if arr[i]==5 and iSFount:
#         max=i
#         iSFount=False
#     i+=1
# print(max)


# find uppercase

# string=input("Enter a string: ")
# result=False
# for i in range(len(string)):
#     if string[i].upper():
#         result=True
# print(result)



# text=input("Enter a text :")
# iStrue=False
# for i in range(len(text)):
#     if text[i].upper()==text[i] and text[i]!=" ":
#         iStrue=True
# if iStrue:
#     print("yes")
# else:
#     print("no")


# def convert(text):
#     iStrue=False
#     for i in range(len(text)):
#         if text[i].upper()==text[i] and text[i]!=" ":
#             iStrue=True
#     return iStrue
# text =str(input("Enter a string: "))
# if convert(text):
#     print("yes")
# else:
#     print("no")



# stop loob when meet upper


def containUpper(text):
    iStrue=False
    for i in range(len(text)):
         if text[i].upper()==text[i] and text[i]!=" ":
             iStrue=True
    return iStrue
isnotUpper=False
while not isnotUpper:
    text=str(input("Enter a string: "))
    if containUpper(text):
        isnotUpper=True
        print("yes")
    else:
        print("no")
