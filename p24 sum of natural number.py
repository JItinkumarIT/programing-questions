#wap to find the sum  of natural number up to num

num=int(input("enter the natural number:"))
if num<0:
    print("enter a positive number")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
        print("the sum is",sum)
    
    
