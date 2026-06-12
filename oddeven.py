num=[34,45,67,76,98,90,83,23,41,13]
odd=0
even=0
for x in num:
    if x%2==0:
        even=even+1
    else:
        odd=odd+1
print(f"We have {even} even numbers")
print(f"We have {odd} odd numbers")