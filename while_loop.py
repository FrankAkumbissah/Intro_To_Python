i = 0
while(i < 10):
    i = i + 1
    print (i)
    
#the first line declares a variable named i and assigns the value 0 to it
#the second line declares a while loop and the parameter is that as long as the value of i
# remains less than 10 the proceeding code should run
# the third line increases the current value of i by 1
# the fourth line prints or displays the value of i on the screen

print("***********************")
print("numbers from 7 to 19")
print("************************")
i = 6
while(i < 19):
    i = i + 1
    print (i)
print("***********************")
print("even numbers between 12 and 20")
print("************************")
i = 12
while(i < 18):
    i = i + 2
    print (i)    
#function that takes two numbers and prints all even numbers between them
def evens():
    start = int(input("Enter the start of the numbers: "))
    end = int(input("Enter the end of the numbers: "))
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num, end = " ")
            for i in num(num, -1, -1):
                print(num)