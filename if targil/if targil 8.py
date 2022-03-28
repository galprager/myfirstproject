num=int(input("enter number:"))
if 10<=num<=99:
    if (num % 10 == 7 or num // 10 == 7) or num % 7 == 0:
     print("lucky number")
    else:
        print("unlucky number")
else:
      print("error")