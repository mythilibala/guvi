s=input()
s1=input()
l=[]
for i in s1:
    l.append(i)
if(len(s1)==len(s)):
   for i in range(len(s)):
       k=ord(s[i])-ord('a')+1
       l[i]=ord(s1[i])+k
for i in l:
   if i>ord('z'):
       i=i-ord('z')+ord('a')-1
   print(chr(i),end="")      
       
       
