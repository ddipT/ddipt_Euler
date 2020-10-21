#Each bnew term in the fib sequence is generated bty adding the previous two terms. By starting with 1 and 2, the first 10 will be .... 
#Consider each and sum whose values do not exceed four million and are even
#Functionised the code
def sum_even_fib():
    fib = [1,2]
    fibeven = []
    flag = True
    i=0
    while flag:
        if (fib[i-1] + fib[i-2]) < 4000000:
            fib.append(fib[i-1] + fib[i-2])
        else:
            flag = False
        

    max = len(fib)
# Storing a list of even numbers
    for x in range(max):
        if fib[x] % 2 == 0:
            fibeven.append(fib[x])


    return sum(fibeven)

print(sum_even_fib())


    
