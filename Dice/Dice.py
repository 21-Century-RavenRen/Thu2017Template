import random
def parseInput(): 
    while True:
        raw = input(":")
        raw = raw.lower()
        raw = raw.split("d")        
        if len(raw)==2:
            try:
                raw[0]=int(raw[0])
                raw[1]=int(raw[1])               
                return raw
            except:
                print("Invalid input.  format example: 4d5.")
        else:
            print("Invalid input.  format example: 4d5.")
            
while True:
    results = parseInput()
    total = 0
    for d in range(results[0]):
        die = random.randint(1,results[1])
        total+= die
        print("Roll is %d" % die)
    print("Total is %d" % total)

