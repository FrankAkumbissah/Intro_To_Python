for  i in range(1, 11):
    print (i)
#it created a for loop with the range starting from 1 and ending at 11
#then we printed the values within the loop

for j in [1, 2, 3]:
    print(j)
#we created a list and using a for loop, displayed the elements of the loop

#this code with range does the same thing
for i in range(1, 4):
    print (i)
    
#[1, 2, 3] this type of data is a list
#range returns integers, or elements in a list

for i in range(0, 20):
   i = i + 2
   print (i)
   

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
        
        
def letter_search():
    text = input("Enter a string: ")
    if (text.count('a') == 0):
        print("False")
    else:
        print("True")
        
def letter_search2():
    text = input("Enter a string: ")
    letter = input("Enter the letter to check presence: ")
    if (text.count(letter) == 0):
        print("False")
    else:
        print("True")
        

def letter_search3():
    text = input("Enter a string: ")
    if (text.count("s") != 0 and text.count("m") != 0):
        print("True")
    else:
        print("False")