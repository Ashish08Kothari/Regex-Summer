
a = int(input("Give a number : "))
b = int(input("Give a number : "))
c = int(input("Give a number : "))

if(a > b and a > c):
  print(f"{a} is biggest")
elif(b > a and b > c):
  print(f"{b} is biggest")
else:
  print(f"{c} is biggest")