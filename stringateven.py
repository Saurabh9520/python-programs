s=input("enter ")
i=0
print("the charcter at even index")
while i<len(s):
    print(s[i])
    i=i+2
i=1    
print("charter at odd")    
while i<len(s):
    print(s[i])
    i=i+2
print('even',s[0::2])
print('even',s[1::2])
