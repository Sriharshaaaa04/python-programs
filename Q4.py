#Q4 to double the string given by the user
def double_string(a):
    c=""
    for i in range(0,len(a)):
        c+=2*a[i]
    return c    
x=input("enter the string:")
y=double_string(x)
print("the result of the operation is ",y)

