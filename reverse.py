def evens():
    start = int(input("Enter the start of the numbers: "))
    end = int(input("Enter the end of the numbers: "))
    for num in range(start, end):
        if num % 2 == 0:
            print(num, end = " ")

def main():
    evens()
    
main()