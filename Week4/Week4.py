'''
Author:Spectraljuice
'''

#1
def g(a,b):
    c = a+b
    return c

print(g(4,5))
print(g(5.2,9.8))
print(g("testing","script"))
print(g(4,"hello"))
#type out the output of the above script:
9
15.0
"testingscript"
ERROR

#2. 
def b(c):
    for x in range(c):
        print(c)

print(b(4))
print(b("h"))
#type out the output of the above script:
4
4
4
4
 ERROR

#3. 
def d(list):
    x = 0
    while x<len(list):
        print(list[x])
        x+=1
        
#This script should print every item in list, but currently contains an error.
#fix this script so it behaves accordingly.


#4. #Write a program which accepts the radius of a circle, and returns the area.
#HINT: the area of a circle is pi*radius*radius
#pi can be estimated at 3.141529
def area(r):
    print(r*r*3.14529)

#5. #Write a function which accepts a list as a parameter.  The function should then
#print out the first and last item of that list.
def headandtail(list):
    print(list[0],list[-1])

#6. #Create a program that asks the user to enter their name and their age. Print 
#out a message addressed to them that tells them the year that they 
#will turn 100 years old.
import datetime
def age():
    age = int (input("What is your age?:")) 
    age = datetime.datetime.now().year-age
    year = age+100
    print(year)
    
# 7. #Write a Python program to check whether a specified value is contained in a 
#group of values: [1, 5, 8, 3].
#Example: -1 should return False
#Example: 3 should return True

