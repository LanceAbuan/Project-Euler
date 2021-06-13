sum = 0;
for i in range (0,1000):
    if (i%3 == 0) or (i%5 == 0):
        print(i)
        sum += i
print()
print("Sum of all multiples of 3 or 5 below 1000 is: " + str(sum))
print()