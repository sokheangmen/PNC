# array1D=["0","0","0","0","*"]
# index = 0
# hasX = True
# while hasX and (index+1)<len(array1D):
#     if array1D[index]=="X":
#         array1D[index] = "0" 
#         array1D[index+1]="X"
#         hasX =False
#     index += 1
# print(array1D)
# def array(array1D):
#     index = 0
#     hasX = True
#     while hasX and (index+1)<len(array1D):
#         if  array1D[index]=="*":
#             array1D[index] = "0" 
#             array1D[index+1]="*"
#             hasX =False
#         index += 1
#     return array1D
# array1D=["0","0","0","0","*"]
# print(array(array1D))
# array1D=[0,0,1]
# position=0
# if position>0 and position<4:
#     array1D[position]=0
#     array1D[position+1]=0
# print(array1D)
# EX2
def positionOFOne (array):
    position=[]
    # changepositions=str(input())
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]==1:
                position.append("*")
                position.append(col)
    return position
array2D=[
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0]
]
print(positionOFOne(array2D))
        
                
