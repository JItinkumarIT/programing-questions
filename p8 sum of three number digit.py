#WAP to sum of digits of three number.

num=234
print(num)
s=0
s = s+num%10
num=num//10

s=s+num%10
num=num//10

s=s+num%10
num=num//10

print('sum of digit',s)




