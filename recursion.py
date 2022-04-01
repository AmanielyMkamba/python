# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number. 
# Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0

def r_sigma(num):
    if num > 0:
        print(num)
        return r_sigma(num - 1) + num    #it adds nums after it / until reaches 0

    return 0    # stop when reach 0 - base case

print(r_sigma(5))



# Recursive Factorial
# Given num, return the product of ints from 1 up to num.
# If less than zero, treat as zero. If not an integer, truncate.
# Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def factorial(num):
    num = int(num)
    if num == 0:
        print(num)
        return 1     #base case
    return factorial(num - 1) * num

print(factorial(6.5))