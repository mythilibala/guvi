import string
n=int(input())
m=list(map(int,input().split(" ")))
l=[]
while(len(m)!=0):
    l.append(str(max(m)))
    m.remove(max(m))
if(l[0]=='0'):
    if(l.count(l[0])==len(l)):
        k=0
        print(k)
else:    
   print("".join(l))     
