def sum(nb1,nb2):
    result=0
    if nb1!=""and nb2!="":
        result=nb1+nb2
    return result
nb1=int(input())
nb2=int(input())
print(sum(nb1,nb2))