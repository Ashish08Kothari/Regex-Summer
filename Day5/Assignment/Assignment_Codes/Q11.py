
p = int(input("Enter price of your product: "))
if(p > 1000):
  print(f"Your final price after 10% discount🎉 is = {0.9 * p}")
elif(p >= 500):
  print(f"Your final price after 5% discount🎉 is = {.95 * p}")