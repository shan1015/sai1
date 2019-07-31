l=int(input())
s=""
k=[]
for i in range(1,l+1):
        if l%i==0:
            s=s+str(i)+" "
print(s.strip())
