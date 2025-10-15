str1=input("Enter first string: ")
str2=input("Enter second string: ")
new_string=str2[0]+str1[1:]+str1[0]+str2[1:]
print(f"String after swapping: {new_string}")