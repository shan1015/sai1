l=int(input())
for  i in range(2,l):
	if l%i==0:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
  #i
