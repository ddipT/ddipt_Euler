"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# Need to implement a way to loop through each series and count the chain length, highest chain length where series start is below a 1000000 wins, so keep a highest counter of the chain, adjust function to output the chain when it's done not the number, but then how do you do it recursively... Need to think about this
def collatz(i):
    print(i)
    if i == 1:
        print("End of Sequence")
        return 1
    if i % 2 == 0:
        return collatz(i/2)
    else:
        return collatz((i*3) + 1)

term = 13

while term != 1:
    term = collatz(term)
    
    

