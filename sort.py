s="b3gds46t"
alph=[]
digi=[]

for ch in s:
    
    if ch.isalpha():
        alph.append(ch)
    else:
        digi.append(ch)
out=''.join(sorted(alph)+sorted(digi))
print(out)
