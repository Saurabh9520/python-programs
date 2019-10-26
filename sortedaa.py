s=input("ener")
prev=s[0]
out=''
c=1
i=1
while i<len(s):
    if s[i]==prev:
        c=c+1
    else:
        out=out+str(c)+prev
        prev=s[i]
        c=1
    if i==len(s)-1:
        out=out+str(c)+prev
    i=i+1
print(out)
        
