#Using the proof that all even numbered palindromes are divisible by 11
#It goes without saying that the largist palindrome made from the product of
#two 3-digit numbers is 6 figures


#checks if a number is palindromic
def is_palindrome(number):
    
    if(number%11 != 0):
        return False

    new_number = 0
    basis = number

    while(basis > 0):
        new_number *= 10
        new_number += (basis%10)
        basis = basis // 10
    
    if(new_number == number):
        return True
    return False


print()
largest_palindrome = 0
for i in range(999,100,-1):
    #We have j start from i to avoid duplicate multiplication
    for j in range(i-1,100,-1):
        product = i * j
        #if the product of i and j is divisible by 11 then it is possibly a palindrome. All even numbered palindromes are divisible by 11. 
        #We can filter out a lot of numbers using this simple rule. Only palindrome check products of 11
        if is_palindrome(product):
            print("product " + str(product) + " is a palindrome")
            if(product > largest_palindrome):
                largest_palindrome = product
                print("New largest palindrome found~! " + str(largest_palindrome))
print("The largest palindrome of two 3 digit numbers is: " + str(largest_palindrome))
print("Finished!\n")
