#Q7 to find the most frequent element in the array 
import statistics
x=int(input("enter the lenght of array :"))
print("inputting the elements in array :")
z=[]
for i in range(0,x):# entering the elements in the array
    c=input()
    z.append(c)
    
y=statistics.mode(z)
print("the frequent element in the string is {}".format(y))

    
    
