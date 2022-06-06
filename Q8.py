#Q8 
a=input("Enter the string")
d=0
for i in range(0,len(a)):
    if a[i].isdigit():
        d=d+int(a[i])
print("The addition is ",d)  