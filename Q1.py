#Q1 to manage the list according to the input of user
def transformation(t,e):
    if e=="Asc":
        t.sort()
        return t
    elif e=="Desc":
        t.sort(reverse=True)
        return t
    else :
        return t
    
x=int(input("enter the total number of elements of array :"))
t=[]
print("start inputing elements")
for i in range(0,x):#entering the elements in list
    c=input() 
    t.append(c)
e=input("enter the operation 1.Asc  , 2. Desc , 3. None :")

f=transformation(t,e)
print("the result is :",f)
    
    
