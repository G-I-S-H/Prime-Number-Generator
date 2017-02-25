#Author: Dustin Grady
#Purpose: To find large prime numbers, and stuff
#Status: Working/ Tested

import sys
import math
import itertools

#saveFile = open("/home/chip/Desktop/primeNumbers.txt", "w")#Open text file in write mode

potentialPrime = 325123621
primeFound = False #Tell us if a prime has been found

def primalityTest(potentialPrime):
    for x in range(2, int(math.sqrt(potentialPrime)+1)): #Check from 2 to the sqrt of the potential Prime
        if(potentialPrime % x == 0):
            primeFound = False
            break
        else:
            primeFound = True

    if(primeFound):
        print(potentialPrime)#Testing
        #with open("/home/chip/Desktop/primeNumbers.txt", "w") as saveFile:
        with open("primeNumbers.txt", "w") as saveFile:
            saveFile.write(str(potentialPrime))#Write prime to file
            saveFile.close()

for potentialPrime in itertools.count(potentialPrime): #Check all numbers >5
    primalityTest(potentialPrime)
