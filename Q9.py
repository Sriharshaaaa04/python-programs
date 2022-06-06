#Q9 to sort the characters of the string
x=input("enter the string")
y=[]
b=""
for i in range(0,len(x)):
    y.append(x[i])
y.sort()
for i in y:
    b+=i
print(b)    
    
