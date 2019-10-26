s=input("enter: ")
out=''
for ch in s:
    if ch.isalpha():
        out=out+ch
        x=ch
    else:
        d=int(ch)
        newc=chr(ord(x)+d)
        out=out+newc
print(out)        
        
