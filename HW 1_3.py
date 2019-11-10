def squaresum(n):
    sqrsum = 0
    
    for a in range(1, n+1):
        sqrsum = sqrsum + (a**2)
    return sqrsum

print ('This function will find square of sums of the first n natural numbers')
n = int(input('Please enter "n" number of natural numbers: ' ))    

print ('The sum of squares is ',squaresum(n))