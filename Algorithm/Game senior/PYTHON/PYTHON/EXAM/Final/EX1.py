arrayOfString=["Lexiaa","Bopha","haha"]
result = []
for arr in arrayOfString:
    sum = 0
    for j in arr:
        if j == "a":
           sum += 1
    if sum == 2:
        result.append(arr)
print(result)