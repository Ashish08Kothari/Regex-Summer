
a = int(input("Enter a number : "))
b = int(input("Enter another number: "))
op = input("Enter the operation you want to perform + - * / : ")
if(op == '+'):
  print(f"{a} + {b} = {a+b}")
elif(op == '-'):
  print(f"{a} - {b} = {a-b}")
elif(op == '*'):
  print(f"{a} * {b} = {a*b}")
else:
  print(f"{a} / {b} = {a/b}")