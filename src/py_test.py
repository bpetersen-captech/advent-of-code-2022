'''
Recursion:
-factorials are recursion
-factorial means multiply initial number by each number smaller than it
-example 5! = 5*4*3*2*1 = 120

Iterative Algorithm:
-iterative means looping
-for factorial example, could do this:
    function getFactorial(5)
        factorial = 1 (running count)
        for x = 1 to 5 (loop)
            factorial = factorial * x (mult nums)

Recursive Algorithm: 
-breaks problem into smaller problems and calls itself to solve each smaller problem
-includes base case and recursive case
-examples 
    - 5! = 5 * 4!
    - 4! = 4 * 3!
    ...
    - 0! = 1 (base case)
    - 1! = 1 (base case)
-for factorial, could do this:
    function getFactorial(n)
        if n < 2, return 1
        else return n * getFactorial(n-1)


'''


import math

x = 5
y = math.factorial(x)
print(x)
print(y)

