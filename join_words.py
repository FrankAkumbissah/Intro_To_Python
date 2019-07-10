#create a list to contain the words
def join():
    frank = []
#loop to input and append the words to elements of the list
    n = int(input("enter the number of elements \n"))
    for i in range(0, n):
        ele = (input())
        frank.append(ele)
#loop to display the words in a list as a sentence
    for i in range(0, n):
        print(frank[i], end=" ")
    
def main():
    join()
    
main()