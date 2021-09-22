#WAP to swap two numbers
'''
x=input('enter x:')  #5
y=input('enter y:') #6

temp=x
x=y
y=temp

print('The value of x after swapping:{}'.format(x))
print('The value of y after swapping:{}'.format(y))

#without use temp
x=5
y=10
x,y=y,x
print("x=",x)
print("y=",y)

#using addition and substraction
x=5
y=10
x=x+y
y=x-y
x=x-y
print("x=",x)
print("y=",y)

#using multiplication and division
x=5
y=10
x=x*y
y=x/y
x=x/y
print("x=",x)
print("y=",y)
'''
#using XOR swap
x=5
y=10
x=x^y
y=x^y
x=x^y
print("x=",x)
print("y=",y)
