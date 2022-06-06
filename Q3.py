#Q3 to do some operation on two numbers 
def op(a,b,c):
    if b=='+':
        return a+c
    elif b=='/':
        return a/c
    elif b=='-':
        return a-c
    else :
        return a or c
    
x=int(input("the first number is :"))
z=int(input("the second number is :"))
y=input("enter the operator +,-,/,or :")
t=op(x,y,z)
print("the result of the operation is :",t)

