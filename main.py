from colorama import Fore,Style

name="Devishi"
print(type(name))

age=14
print(type(age))

height=5.3
print(type(height))

student=True
print(type(student))

print(f"{Fore.BLUE} My name is ",name)
print(f"{Fore.GREEN}My age is ",age)
my_friends=["Aisha","Tvishha","Aarushi"]
print(type(my_friends))
print(f"{Fore.YELLOW}My friends are" ,my_friends)
my_friends.append("Aditi")
print(my_friends)
my_friends.remove("Aarushi")
print(my_friends)
num=[1,2,3,4,5,6,7,8,9,10]

print(num[3:5])