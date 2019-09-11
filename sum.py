num=int(input("please enter the no"))
sum=0
while(num > 0):
    rem = num%10
    sum=sum+rem
    num=num//10
print("::",sum)    
#

Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)

#
binary=input('enter number in binary format')
temp=int(binary,2)
print(binary,"in octal=",oct(temp))

#
PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
circumference = 2 * PI * radius

print(" Area Of a Circle = %.2f" %area)
print(" Circumference Of a Circle = %.2f" %circumference)
