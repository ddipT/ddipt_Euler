#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?


num = 600851475143 
num2 = num
counter = 2

largestfactor = 0

while(counter * counter <= num2):
    if num2 % counter == 0:
        num2 = num2/counter
        largestfactor = counter
    else:
        counter+=1

if num2 > largestfactor:
    largestfactor = num2

print(largestfactor)