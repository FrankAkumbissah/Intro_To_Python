#i = 10
#while(i < 20):
 #   i = i + 2
  #  print (i)

def evens():
    start = int(input("Enter the start of the numbers: "))
    end = int(input("Enter the end of the numbers: "))
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num, end = " ")
            num2 = num
            num2 = str(num2)

def stars():
    i = 4
    while(i > 0):
        print ("****")
        i = i - 1
        
def stars2():
    for i in range (0, 4):
        for j in range(0, i + 1):
            print("*", end = ' ')
        print("\n")
    for i in range (0, 4):
        for j in range(i + 1, 4):
            print("*", end = ' ')
        print("\n")
def main():
    stars2()
    
main()