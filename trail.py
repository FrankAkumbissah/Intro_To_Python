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
            
               
def main():
    evens()
    
main()