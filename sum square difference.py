#https://projecteuler.net/problem=6

#The sum of the squares of the first ten natural numbers is,
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(j):

    squares = []
    total = 0
    sqsum = 0

    for i in range(j):
        i += 1
        total += i 
        #add to list of the squares
        squares.append(i**2)

    # Calculate the square of the sum
    sqsum = total ** 2

    #calculate difference
    return(sqsum - sum(squares))



print(sum_square_difference(100))

    


