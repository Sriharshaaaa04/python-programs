#Q6 prime numbers
k=int(input("Enter the starting element of range :"))
h=int(input("Enter the ending element of the range :"))
b=[]
for i in range(k,h+1):
    a=0
    for j in range(2,i//2+1):
        if i%j==0:
            a+=1
            break
    if (a==0 and i!=1):
        print("%d" %i,end='  ')
    
    
