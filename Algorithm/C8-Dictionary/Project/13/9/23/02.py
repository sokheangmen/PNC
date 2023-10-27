fruit=[{'name':'Orange','Quantity':16},
       {'name':'Orange','Quantity':4}
       ]
total=0
for fruitName in fruit:
    total+=fruitName['Quantity']
print(total)