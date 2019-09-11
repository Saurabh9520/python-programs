year=int(input())
if((year%400 == 0)) or ((year%4 == 0) and (year%100 != 0)):
    print(year)
else:
    print("not",year)

#gcd

x=int(input("enter the no"))
y=int(input("enter the no"))
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1,smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i        
print(hcf)    

# Python Program to find LCM of Two Numbers

num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

a = num1
b = num2

while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

gcd = num1
print("\n GCD of {0} and {1} = {2}".format(a, b, gcd))

lcm = (a * b) / gcd
print("\n LCM of {0} and {1} = {2}".format(a, b, lcm))


##
num = int(input("Enter a number: "))
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")
