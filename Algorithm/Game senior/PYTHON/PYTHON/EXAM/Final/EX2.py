# def reverseText(text):
#     data=[]
#     for arr in text:
#         getReuslt=""
#         getReuslt+=(arr[::-1])
#         data.append(getReuslt)
#     return data
# text=["abc", "123", "456","hello"] 
# reverseArray=reverseText(text)
# print(reverseArray[::-1])


def reverseText(text):
    getReuslt=""
    for arr in range(1,len(text)+1):
        getReuslt+=text[-(arr)]
    return getReuslt
text=["abc", "123", "456","hello"] 
# reverseArray=reverseText(text)
newarray=[]
for i in range(1,len(text)+1):
    newarray.append(reverseText(text[-(i)]))
print(newarray)

