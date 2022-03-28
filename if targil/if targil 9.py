d=int(input("enter day:"))
if 1 > d or d > 31:
    print("error in the day")
m=int(input("enter mount:"))
if 1 > m or m > 12:
    print("error in the mount")
y=int(input("enter year:"))
if 1950 > y or y > 2020:
    print("error in the year")

if 1<=d<=31 and 1<=m<=12 and 1950<=y<=2020:
   if d<10 and m>10:
    print(f"0{d}/{m}/{y%100}")
   if d>10 and m<10:
       print(f"{d}/0{m}/{y % 100}")
   if m<10 and d<10:
        print(f"0{d}/0{m}/{y%100}")




