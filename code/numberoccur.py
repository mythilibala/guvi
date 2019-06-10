s=input()
k=[]
for i in s:
    k.append(i)
l=k
for i in k:
    n=k.count(i)
    for j in range(n-1):
        l.remove(i)
print(len(l))        
