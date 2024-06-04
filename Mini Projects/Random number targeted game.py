import random

target = random.randint(1,50)

while True:
    myChoice = input("Guess the target or Quit(Q) :")
    if(myChoice == "Q"):
         break
    myChoice = int(myChoice)
    if(myChoice == target):
         print("Sucess: Correct Guess!!!")
         break
    elif(myChoice<target):
         print("Entered number is small.Take a bigger....")
    else:
         print("Entered number is big.Take a smaller....")
    
print("----------GAME OVER----------")