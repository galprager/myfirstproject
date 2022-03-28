from random import randint
num= randint(1,9)
print(num)
guess= int(input("guess number:"))
while guess!=num:
    if guess>num:
        print("You have selected a higher number")
    if guess<num:
        print("You have selected a lower number")
    guess = int(input("guess number:"))
else:
    print("Equal number")