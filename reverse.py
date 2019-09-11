#reverse a string.
def reverse(s):
    str=""
    for i in  s:
        str=i+str
    return str
s="geeks"
print("the original")
print(s)
print("the reversed string ::",end="")
print(reverse(s))

#----------------------
s=input("enter a string: ")
print(s[::-1])
print(len(s))
print(s.count(" "))
