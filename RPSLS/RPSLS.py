'''
Created on Dec 7, 2017

@author: ncarlson
'''
import random
choices = {1:"Rock",2:"Paper",3:"Scissors",4:"Lizard",5:"Spock"}
killers = {1:[2,5],2:[3,4],3:[1,5],4:[1,3],5:[2,4]}
calc = {1:0,2:0,3:0,4:0,5:0}
while True:
    ai = 1
    for c in calc.keys():
        if calc[c]>calc[ai]:
            ai = c
    randomChoice = random.randint(0,1)
    ai = killers[ai][randomChoice]
    for i in choices.keys():
        print("%d: %s" % (i,choices[i]))
    guess = input(":")
    try:
        guess = int(guess)
        if guess<1 or guess>5:
            raise Exception("invalid input")
        else:
            calc[guess]+=1
            print("Well I chose %s" % choices[ai])
            if ai==guess:
                print("We Tied!!!")
            else:
                if guess in killers[ai]:
                    print("You Win!!!")
                else:
                    print("You Lose!!!")
    except:
        print("Choose a number between 1 and 5.")
    
    
        
    