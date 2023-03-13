c = open("item.txt","r")
count = 0
extpricesum = 0
itemid=str(c.readline().rstrip('\n'))
print("order summary: \n")

while itemid !="":
  qty=int(c.readline())
  price=int(c.readline())
  extprice=qty*price
  extpricesum=extpricesum+extprice
  count=count+1
  print(f"item: {itemid}")
  print(f"quantity: {qty}")
  print(f"price: ${price:.2f}")
  print(f"total price: ${extprice:.2f}\n")
  itemid=str(c.readline())
c.close()
avg = extpricesum/count

print(f"the sum of all orders is ${extpricesum:.2f}")
print(f"there were {count} number of orders")
print(f"the average order is ${avg:.2f}")
  