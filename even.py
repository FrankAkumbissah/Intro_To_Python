from map import too_old
def is_even(number):
    if (number % 2 == 0):
        print("It's an even number")
    else:
        print("It's an odd number")
        
def main():
    ask = float(input("Enter a number: "))
    is_even(ask)
    not(ask)
    

from map import too_old
main()
numbers = [1,56,234,87,4,76,24,69,90,135]
print("The even numbers are: ",[num for num in numbers if num % 2 == 0])
print("The odd numbers are: ",[num for num in numbers if num % 2 != 0])
#combinations using the is not function
print("The odd ones are: ", [num for num in numbers if num % 2 is not 0])
too_old(15)