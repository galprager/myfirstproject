guess= int(input("Guess a number between 0 to 100:"))
from random import randint
num= randint(0,100)
print(num)
print("a.lower/b.higher/c.equal number?")
numguess=input("chooes answer:")
while numguess!="c":
    guess = int(input("Guess a number between 0 to 100:"))
    num = randint(0, 100)
    print(num)
    print("a.lower/b.higher/c.equal number?")
    print("a/b/c ?")
    numguess = input("chooes answer:")
else:
    print("success")
