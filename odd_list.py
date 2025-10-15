num_list=input("Enter numbers(put space in btw): ").split(" ")
odd_list=[]
for num in num_list:
    if(int(num)%2!=0):
        odd_list.append(num)
print("List after removing even no.s: ",odd_list)
