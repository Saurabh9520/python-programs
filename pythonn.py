import sys
word1=input("enter the first word")
word2=input("enter the second ")
word3=input("enter the third")
for ch in word1:
    
if ch in "aeiouAEIOU":
word1=word1.replace(ch,"$")

for ch in word2:
if ch in "aeiouAEIOU":
word2=word2.replace(ch,"#”)

for ch in word3:
if ch in "abcdefghijklmnopqrstuvwxyz”:
word3=word3.upper()
print(word1,word2,word3)
