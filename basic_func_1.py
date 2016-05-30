#Mapping
def add1(x):
    return x+1
print map(add1, [1,2,3,4,5])

#Filtering
def isOdd(x):
    return x % 2 == 1
print filter(isOdd, range(1,20))

#Reduce
def add(x,y):
    return x+y
print reduce(add, range(1,100))

#Lambdas
print map(lambda x: x + 1, range(1,20))

print filter(lambda x: x % 2 == 1, range(1,20))

print reduce(lambda x,y: x + y, range(1, 100))

#Nested functions with lambdas

print reduce(lambda x,y: x + y, map(lambda x: x + 1, range(1,10)))