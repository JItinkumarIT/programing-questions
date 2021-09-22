#WAP TO FIND THE LARGEST NUMBER AMONG THREE NUMBER
n1=float(input("Enter the First Number:"))
n2=float(input("Enter the second Number:"))
n3=float(input("Enter the Third Number:"))
if(n1>=n2 and n1>=n3):
    largest=n1
if(n2>=n3 and n2>=n1):
    lagerst=n2
if(n3>=n1 and n3>=n2):
    largest=n3
print("The largest Number is:",largest)    
