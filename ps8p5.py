c = open("students.txt")
count = 0
sumtuition = 0

while lastname!="":
  district=str(f.readline())
  credits=int(f.readline())
  if 'in' in district:
    creditprice = 250
  else:
    creditprice = 500
  tuition=credits*creditprice
  count = count+1
  print(f"student name: {lastname}")
  print(f"credits taken: {credits}")
  print(f"tuition due: ${tuition:.2f} \n")
  sumtuition=sumtuition+tuition
  lastname=str(f.readline())

f.close()

print(f"number of students: {count}")
print(f"the sum of the tuition is ${sumtuition:.2f}")