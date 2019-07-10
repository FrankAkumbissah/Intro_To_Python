def calculate():
    ask = input("What do you want to do?:\n ADD \t\t\t SUBTRACT \n MULTIPLY \t\t\t DIVIDE\n")
    if (ask == "ADD"):
        print(add())
    elif (ask == "SUBTRACT"):
        print(subtract())
        
    elif (ask == "MULTIPLY"):
        print(multiply())
        
    elif (ask == "DIVIDE"):
        print(divide())
    
    else:
        print("Invalid input please try again")
        
def add():
    first = int(input("Enter the first value \n"))
    second = int(input("Enter the second value \n"))
    sum = first + second
    return sum

def subtract():
    first = int(input("Enter the first value \n"))
    second = int(input("Enter the second value \n"))
    difference = first - second
    return difference

def multiply():
    first = int(input("Enter the first value \n"))
    second = int(input("Enter the second value \n"))
    product = first * second
    return product

def divide():
    first = int(input("Enter the first value \n"))
    second = int(input("Enter the second value \n"))
    dividend = first / second
    return dividend

def main():
    print("*********************************************************")
    print("PLEASE MAKE SURE TO TYPE YOUR RESPONSE IN CAPITAL LETTERS")
    print("*********************************************************")
    calculate()
    
main()