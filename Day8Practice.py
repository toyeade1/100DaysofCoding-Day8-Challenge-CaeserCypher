#coding challenge 1

#import math


#def paint_needed(height,width):
    #coverage = 5
    #number_of_cans = math.ceil((height * width) / coverage)
    #print(f'You\'ll need {number_of_cans} cans of paint for your {height} by {width} wall')

#paint_needed(7,13)

#Coding Challenge 2: Prime number checker

def prime_checker(number):
    isPrime = True
    for num in range(2,number):
        if number % num == 0:
            isPrime = False
    if isPrime:
        print(f'{number} is a prime number.')
    else:
        print(f'{number} is not a prime number.')



n = int(input('Check this number: '))
prime_checker(number=n)


