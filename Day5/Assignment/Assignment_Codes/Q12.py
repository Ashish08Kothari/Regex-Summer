
m = input("Enter any month: ").lower()
if(m == "january" or m == "march" or m == "may" or m == "july" or m == "august" or m == "october" or m == "december"):
  print(f"{m} has 31 days")
elif(m == "april" or m == "june" or m == "september" or m == "november"):
  print(f"{m} has 30 days")
else:
  print(f"{m} has 28 days")