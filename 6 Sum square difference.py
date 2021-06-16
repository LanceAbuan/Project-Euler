#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_diff(number):
    #sum_squared = the sum of the numbers, squared
    square_of_sum = ((1+number)*(number/2))**2

    #square_sum = numbers squared, summed
    sum_of_squares = 0
    for i in range (1,number+1):
        sum_of_squares += i**2

    print(square_of_sum - sum_of_squares)
    

sum_square_diff(100)