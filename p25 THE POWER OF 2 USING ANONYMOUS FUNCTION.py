#WAP DISPLAY THE POWER OF 2 USING ANONYMOUS FUNCTION

terms=int(input('How many ters?'))
result=list(map(lambda x: 2**x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
    print("2 raised to power",i,"is",result[i])

         
