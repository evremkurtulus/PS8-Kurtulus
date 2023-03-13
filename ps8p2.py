numa=0
numb=1

for count in range(1,21,1):
   numc=numa+numb
   print(f"#{count} - {numc}")
   numa = numb
   numb=numc