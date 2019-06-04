n=int(input())
k=int(input())
m=[]
for i in range(n):
  j=int(input()) 
  m.append(j)
s=0  
for i in range(k):
    s=s+m[i]
print(s)    
