num=[15,22,37,40,55,63,78]
odd=[]
even=[]
divisible=[]
for x in num:
    if x%2==0:
        even.append(x)
    elif x%3==0:
        divisible.append(x)
    else:
        odd.append(x)
print(f"even no.s= ",even)
print(f"odd no.s=  ",odd)
print("no.s divisible by 3= ",divisible)