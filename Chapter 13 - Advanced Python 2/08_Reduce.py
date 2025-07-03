from functools import reduce
l = [1,2,3,4,5]
sum = lambda a,b:a+b
mul = lambda a,b:a*b
print(reduce(sum, l))
print(reduce(mul, l)) # --> Factorial of len(l)

# sum(1,2) = 3
# sum(3,3) = 6
# sum(6,4) = 10
# sum(10,5) = 15
