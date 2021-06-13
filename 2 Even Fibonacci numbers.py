sum = 2
#we add from the third term and onward, so sum needs to be 2 at the start
#this isn't a function so we don't need to store fib numbers for speed

fib1 = 1
fib2 = 2
temp = 3

while temp < 4000000:
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    print(temp)
    if temp%2 == 0:
        sum+=temp
print("Sum of even fib numbers: " + str(sum) )