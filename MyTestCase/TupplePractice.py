
'''
Created on May 18, 2018

@author: aranjan
'''
#A list is a collection which is ordered and unchangeable. 
#In Python lists are written with round brackets.
thisTupple = ("apple", "banana", "cherry")
print(thisTupple)
#this is unchangebale so below code will show error
#thisTupple[1]='mango'
#print(thisTupple)

print(len(thisTupple))

#Constructer list
thisTupple=tuple(("hello","hi","bye"))
print('Tuples',thisTupple)
print("Size of tuples",len(thisTupple))

# Iterate a tupple
for tupl in thisTupple: print(tupl)