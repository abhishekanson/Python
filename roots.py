import math
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d=b*b-4*a*c
if d>0: #distinct roots
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
    print("Distinct roots r1=",r1,"r2=",r2)
elif d==0: 
    r=(-b+math.sqrt(d))/2*a
    print("Same roots r=",r)
else: 
    real=-b/2*a
    img=math.sqrt(-d)/2*a
    print("complex roots")
    print(f"{real}+{img}i and {real}-{img}i")

