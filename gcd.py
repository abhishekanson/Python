a=int(input("Enter first no.: "))
b=int(input("Enter second no.: "))
smaller=min(a,b)
gcd=0
for i in range(1,smaller+1):
    if(a%i==0 and b%i==0):
        gcd=i
print(f"GCD of {a} and {b} = {gcd}")