billamt=float(input("Enter the bill amount"))
userpaid=float(input("Enter the amount the user paid"))
change=billamt-userpaid
Rs500=change//500
newnumber=change%500
Rs100=newnumber//100
newnumber=newnumber%100
Rs50=newnumber//50
newnumber=newnumber%50
Rs10=newnumber//10
newnumber=newnumber%10
print("No. of 500s is ",Rs500)
print("The no. of 100s is ",Rs100)
print("The no. of 50s is ",Rs50)
print("The no. of 10s is ",Rs10)
print("The no. of ones is ",newnumber)