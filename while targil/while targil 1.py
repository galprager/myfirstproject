num=int(input("please enter number:"))
while 100<=num<=999:
    print(num//100+num%10+num//10%10)
    num=int(input("please enter number:"))
print("faild")