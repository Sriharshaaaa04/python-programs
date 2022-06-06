#Q2 to replace the initial 12 numbers of the credit card by *
def card(a):
    c=""
    for i in range(0,16):
        if i>=12:
            c+=a[i]
        else:
            c+='*'
    return c        

x=input("enter cerdit card number :")
d=card(x)
print("the result of the opeation is :",d)
