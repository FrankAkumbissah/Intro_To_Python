names = ["sam", "john", "james"]
print(list(map(len, names)))

'''def sqr(x):
    return x ** 2
    map (sqr, map(len, names))

sqr()'''

items = [1, 2, 3, 4, 5]
squares = list(map((lambda x: x ** 2), items))
print(squares)

def too_old(x):
    return x > 30
    ages = [22, 25, 29, 56, 24, 12]
    list(filter(too_old, ages))

too_old():