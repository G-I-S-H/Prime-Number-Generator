#Author: Dustin Grady
#Purpose: To find large prime numbers
#Status: Working/ Tested

import sys
import math
import itertools

potentialPrime = 325123621 #Current largest prime found
primeFound = False #Tell us if a prime has been found

def primalityTest(potentialPrime):
    for x in range(2, int(math.sqrt(potentialPrime)+1)): #Check from 2 to the sqrt of the potential Prime
        if(potentialPrime % x == 0):
            primeFound = False
            break
        else:
            primeFound = True

    if(primeFound):
        print(potentialPrime) #For testing purposes
        #with open("/home/chip/Desktop/primeNumbers.txt", "w") as saveFile:
        with open("primeNumbers.txt", "w") as saveFile:
            saveFile.write(str(potentialPrime)) #Write prime to file
            saveFile.close()

for potentialPrime in itertools.count(potentialPrime): #Recursive call to primalityTest
    primalityTest(potentialPrime)
