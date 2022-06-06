#Q5 to find the repeating number in a array of lenght 100
print("start inputing the numbers")
x=[]
for i in range(0,100):
    c=input()
    x.append(c)
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j] :
            print("the number which is recurring is : {}".format(x[i]))
            break
        else :
            continue
