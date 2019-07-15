'''numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print([num for num in numbers if num >= 0])
print([num for num in numbers if num % 2 == 0]) '''


answer = int(input("Enter a number: "))
while answer != 0:
    number = int(input("Enter a number: "))
    if(number % 2 == 0):
        print("It's an even number")
        break
    else:
        print("It's an odd number")
        break
    