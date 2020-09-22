## Lesson 2, Exercise 2.4 Fibonnaci Series
## By: B. Matthews
## 9/11/2020

def fibonacci(n):
#"""Generates a Fibonnaci series with length n"""

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
#"""Generates a Lucas series with length n"""
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series (n, a=0, b=1):
    #"""Generates a series with first two numbers that user specifies"""
    if (n == 0):
        return a
    elif (n == 1):
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)


##Test the function
#n = int(input("Enter a number >> "))

#for i in range (n+1):
    #print (lucas(i))

#print ("Fibonacci:", n,"th value is: ", fibonacci(n))#

#print ("Lucas series: ", lucas(n))

##Test using the assert template
if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("Tests passed!")

