def reverString(word):
    res=""
    for i in range(1,lenght+1,1):
        if i <= len(word):
            res += word[lenght -i ]
    return res
word = input()
lenght = len(word)
print(reverString(word))