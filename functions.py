num1=float(input("Enter the 1st number: "))
num2=float(input("Enter the 2nd number: "))

print("Pick your choice: 1.Add 2.Subtract 3.Multiply 4.Divide")
def add(a,b):
    print("a+b= ",a+b)
choice=int(input("Enter your choice:"))
if choice==1:
    add(num1,num2)

