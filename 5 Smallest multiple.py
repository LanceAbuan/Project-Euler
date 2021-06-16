#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#We could brute force, and we can also go up by intervals of 2520 (since all intervals will be even divis by 1...10 w/o a remainder)
#I'm not sure how else to do it. If I relook, I'll give it another shot.

i = 0
notfound = True
while notfound:
    #we don't need to check if i is divisible by 1-10 since it will be (intervals of 2520)
    i+=2520
    notfound = False
    for j in range (11,20):
        print(j)
        if i % j != 0:
            notfound = True
            break
        print("Testing " + str(i))

        

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is " + str(i))