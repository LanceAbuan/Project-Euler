#What is the largest prime factor of the number 600851475143 ?
#Naive approach, check numbers in range of 1 to sqrt of 600851475143
#Any integer greater than 1 is either a prime number, or can be written as a unique product of prime numbers (ignoring the order).
#We can use the above fact to find the largest possible prime
#20 can be divided by 2, which results in 10
#10 can be divided by 2, which results in 5
#5 is a prime and also the largest prime is left.

#33 can be divided by 3, which results in 11
#11 is a prime and also the largest prime is left.

basis = 600851475143
largest_prime = 0

i = 2
#line 2 logic
while i^2 < basis:
    #applies logic from lines 5->10
    if(basis%i == 0):
        basis = basis/i
        largest_prime = i
    else:
        #divide by i until you can't anymore, this iterates through and up
        i+=1

if basis > largest_prime:
    largest_prime = basis
print("\nlargest prime factor of 600851475143 is " + str(largest_prime)+"\n")
