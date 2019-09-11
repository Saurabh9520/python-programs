lst=[]
for num in range(1,100):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break
            
    
        else:
            print(num)
            lst.append(num)
   
print(lst)
sum=0
for i in lst:
    sum=sum+i
print(sum)    
#prime
num = int(input("number"))
for i in range(2,num):
    if num%i == 0:
        print("not prime no")
        break
else:
    print("prime")

#factorial
num =int(input("enter the no"))
fac = 1
for i in range(1,num+1):
    fac=fac*i
print(fac)    
    
