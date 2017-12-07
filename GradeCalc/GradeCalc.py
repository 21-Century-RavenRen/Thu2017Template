'''
@author: Carlson
@description: Create an application which will continuously ask for grades 
(0-100) for assignments.  Once the user inputs a 'q', the program should output 
the average of all of the input grades.
'''
grades = []
limit = 10000
letters = {0:"F",60:"D",70:"C",80:"B",90:"A"}
while True:
    if len(grades)>limit:
        break
    grade = input("Input grade (0-100) or q to quit:")
    if grade.lower()=="q":
        break
    try:
        grade = int(grade)
        if grade<0 or grade>100:
            raise Exception("Not valid number")
        else:
            grades.append(grade)
    except:
        print("hey genius, I said a number between 0 and 100.  Try again.")

sum = 0
if len(grades)>0:
    for grade in grades:
        sum+=grade
    average = sum/len(grades)
    letter = 0
    for l in letters.keys():
        if l<=average and l>letter:
            letter = l
    print("Score: %d %s" % (average,letters[letter]))
    
    