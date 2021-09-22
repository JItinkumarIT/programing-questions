#WAP TO CHECK INPUT NUMBER IS PRIME OR NOT
'''
num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num)
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")

'''



#WAP TO FIND THE PRIME NUMBER IN GIBVEN INTERVAL
lower=900#int(input("enter the lower number:"))
upper=1000#int(input("enter the upper number:"))

print("Prime numbers between",lower, "and" ,upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
            else:
                print(num)
    
    
