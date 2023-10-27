
words = eval( input('Enter the words: ') )       

filteredWords = []

for arr in words:
    letterA = 0
    letterB = 0
    for i in arr:
        if i == "A":
            letterA += 1
        elif i == "B":
            letterB += 1 
    if letterA == 2 and letterB == 1:
        filteredWords.append(arr)
print(filteredWords)
