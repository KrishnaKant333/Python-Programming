l = [5, 3,4 ,45 ,525, 43,4, 785]

divBy5 = lambda x:x%5==0

divList = filter(divBy5, l)
print(list(divList))
