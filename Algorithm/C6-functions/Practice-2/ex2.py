def getComment(grade):
    result="bad"
    if grade>10:
        result="good"
    return result
grade=int(input())
print(getComment(grade))