s='a4b3c2'
out=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        out=out+x*d
output=''.join(sorted(out))
print(out)
