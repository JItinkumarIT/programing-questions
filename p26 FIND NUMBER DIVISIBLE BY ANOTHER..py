#WAP  TO FIND NUMBER DIVISIBLE BY ANOTHER.

n=int(input("enter the divisible number:"))
my_list=[12,65,54,39,110,339,221]
result=list(filter(lambda x:(x%n==0),my_list))
print("numbers divisible by",n,"are",result)
