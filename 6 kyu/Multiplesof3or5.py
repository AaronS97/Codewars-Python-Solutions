# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If a number is a multiple of both 3 and 5, only count it once.

# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    s = 0
    if number < 0:
        return 0
    else:
        for n in range(1,number):
            if n > 0 and (n % 3 == 0 or n % 5 == 0):
                s+=n
            else:
                pass
        return(s)

if __name__=="__main__":
    solution(30)