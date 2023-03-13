if = open("name.txt","r")
bonussum=0
lastname=str(f.readline().rstrip('\n'))

while lastname!="":
  salary=int(f.readline())
  if salary >= 100000:
    bonusrate = 0.2
  elif salary >= 50000:
    bonusrate = 0.15
  else: 
   bonusrate = 0.1
  bonus = salary*bonusrate
  print(f"name: {lastname}")
  print(f"salary: ${salary:.2f}\n")
  print(f"bonus: ${bonus:.2f}\n")
  bonussum=bonussum+bonus
  lastname=str(f.readline())
f.close()
print(f"the total amount of bonuses given out is ${bonussum:.2f}.")