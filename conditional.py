i = 8
if(i % 2 == 0):
    print ("Even Number")
else:
    print ("Odd Number")
# % is the modulo
# i % 2 checks and returns the modulo or remainde of the operation i / 2

def evens():
    frank = []
    n = int(input("enter the number of elements \n"))
    for i in range(0, n):
        num = int(input())
        frank.append(num)
    