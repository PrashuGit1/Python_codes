import random

j=1
cp=0
hp=0
print("\t \t \t Welcome TO sanack water gun Game \n \n ")
print("\t\t\t Developed By- Prakash Shukla \n \n \n")
while(j<=10):
    print("Enter your choise")
    i=int(input("1 for snack and 2 for Water and 3 for Gun: "))
    r=random.randint(1,3)
    if(i==r):
        print("\n Same choise \n")
        print(f"you have left now: {10-j} chance \n\n")


    elif(i==1 and r==2):
        hp=hp+1
        print("\n Your's partner choise is:- Water \n")
        print("you Win")
        print("you got one point\n")
        print(f"you have left now: {10-j} chance \n\n")
    elif(i==1 and r==3):
        cp=cp+1
        print("\n Your's partner choise is:- Gun\n")
        print("you lose")
        print("Your's patner got 1 point \n")
        print(f"you have left now: {10-j} chance \n\n")



    elif(i==2 and r==1):
        cp=cp+1
        print("\n Your's partner choise is:- Snack \n")
        print("you Lose")
        print("your's partner got 1 point \n")
        print(f"you have left now: {10-j} chance \n\n")
    elif(i==2 and r==3):
        hp=hp+1
        print("\n Your's partner choise is :- Gun \n")
        print("You won ")
        print("you got 1 point \n")
        print(f"you have left now: {10-j} chance \n\n")


    elif(i==3 and r==1):
        hp=hp+1
        print("\n Your's partner choise is :- Snack \n")
        print("you won ")
        print("you got 1 point \n")
        print(f"you have left now: {10-j} chance \n\n")
    elif(i==3 and r==2):
        cp=cp+1
        print("\n Your's partner choise is :- Water \n")
        print("you Lose")
        print("Your's partner got 1 point \n")
        print(f"you have left now: {10-j} chance \n\n")

    else:
        print("\n Invalid input! \n")
        print(f"you have left now: {10-j} chance \n")
        continue
        

    j=j+1
print(f"\n your score : {hp}  computer's score : {cp} \n")

if(hp>cp):
    print("\t \t\t you won ")
elif(hp<cp):
    print("\t\t\t your's partner win ")
else:
    print("\t\t\t\t It's tie!")
