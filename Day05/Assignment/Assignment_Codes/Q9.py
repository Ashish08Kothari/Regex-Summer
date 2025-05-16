
a = int(input("Enter 1st side of triangle: "))
b = int(input("Enter 2nd side of triangle: "))
c = int(input("Enter 3rd side of triangle: "))
if(a < b+c or b < a+c or c < a+b):
  print("Yes its a Triangle")
else:
  print("It's not a Triangle")