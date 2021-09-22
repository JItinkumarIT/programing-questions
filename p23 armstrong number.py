#WAP TO CHECK IF TBE NUMBER IS ARMSTRONG OR NOT
'''
num = int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
            
'''

#WAP TO CHECK ARMSTRONG NUMBER IN A GIVE INTERVAL

lower=int(input("ENTER THE FIRST VALUE: "))
upper=int(input("ENTER THE SECOND VALUE: "))
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
        if num==sum:
            print(num)
