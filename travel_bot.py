from colorama import Fore,Style
import random
travel_blog={
    "beaches":["Maldives","Miami Beach","Coral reef"],
    "mountains":["Mt.Everest","Kanchenjunga","Kilimanjaro","Peru"],
    "cities":["Mumbai","NYC","Spain"],
}
print(f"{Fore.BLUE}Welcome to my travel bot!,{Style.RESET_ALL}")
while True:
    print(f"{Fore.RED}Where would you like to go? 1.Beaches 2.Mountains 3.Cities{Style.RESET_ALL}")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("How about ",random.shuffle(travel_blog["beaches"]))
    elif choice==2:
         print("How about ",random.shuffle(travel_blog["mountains"]))
    elif choice==3:
         print("How about ",random.shuffle(travel_blog["cities"]))
    else:
        print("wrong choice")
    r=input("Do you like the suggestion? Enter yes or no")
    if r=="yes":
        print("Glad to assist you!")
        break
    
    
    