#! usr/bin/env python3

#Lexi Rossow
#PE2
#January 17, 2023; modified on January 23, 2023
#Random Lottery Ticket numbers



import random
from random import randint

#constants
LIMIT = 60
DIGITS = 5
POWERBALL = 0

#empty stats list
stats = []


#user prompt
TICKET = int(input("How many lottery tickets would you like? "))
print()

#number of tickets requested
for ticket in range(1, TICKET+1):
    listinglist = []
#generate lottery ticket digits nested inside 
    for count in range(1, DIGITS+1):
        listinglist.append(randint(1, LIMIT))

    #return the user's tickets
    print(str(ticket) + ": " + str(listinglist))

    #ticket summary
    print("Ticket Summary:", end="\n")

    #Powerball
    print("Powerball:", random.randint(1,60))
    
    #mean
    mean = (sum(listinglist)) / len(listinglist)
    print("Mean:", mean)

    #median
    listinglist.sort()
    median = (len(listinglist)) / 2
    print("Median:", median)

    #min and max
    minNUM = min(listinglist)
    maxNUM = max(listinglist)
    print("Min:", minNUM)
    print("Max:", maxNUM)

    #store the stats 
    stats.append(mean)
    stats.append(median)
    stats.append(minNUM)
    stats.append(maxNUM)
    #print(stats)
    print()
    print()
    

##OUTPUT:
##1: [56, 42, 3, 55, 5]
##Ticket Summary:
##Powerball: 22
##Mean: 32.2
##Median: 2.5
##Min: 3
##Max: 56
##
##
##2: [34, 1, 37, 5, 30]
##Ticket Summary:
##Powerball: 46
##Mean: 21.4
##Median: 2.5
##Min: 1
##Max: 37
##
##
##3: [7, 40, 13, 16, 47]
##Ticket Summary:
##Powerball: 54
##Mean: 24.6
##Median: 2.5
##Min: 7
##Max: 47
    



