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

def reverse_evens():
    start = int(input("Enter the start of the numbers: "))
    end = int(input("Enter the end of the numbers: "))
      
    for num in range(start + 1, end):
        if num % 2 == 0:
            reverse = ''
            for i in range(len(num), 0, -1):
                reverse += num[i-1]
            print(int(reverse))
            
    
def main():
    evens()
    
main()