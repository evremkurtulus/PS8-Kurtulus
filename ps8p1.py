principle = int(input("what was the initial investment? "))
rate = float(input("what was the interest rate? "))

totalint=0

for count in range(1,6,1):
  interest = principle*rate
  endbal = principle+interest
  print(f"Year: {count}   principle: ${principle:.2f}   ending balance: ${endbal :.2f}")
  principle = endbal
  totalint = totalint + interest

print(f"the total interest accumulated is {totalint:.2f}.")