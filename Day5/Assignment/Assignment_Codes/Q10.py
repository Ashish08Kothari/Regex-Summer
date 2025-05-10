
w = int(input("Enter your weight in KG's: "))
h = int(input("Enter your height in meters: "))
bmi = w / h**2
if(bmi >= 30):
  print("obesity")
elif(bmi >= 25):
  print("Overweight")
elif(bmi >= 18.5):
  print("Normal weight")
else:
  print("Underweight")