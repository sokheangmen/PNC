def removeMinus(word):
    newWord=""
    for i in range(len(word)):
        if word[i]!="-":
            newWord+=word[i]
    return newWord

isContinue = True
while isContinue:
    word = input()
    print(removeMinus(word))
    choice = isContinue
    choice=input("Do you want to continue?Y/N")
    if choice =="N":
        isContinue =False

