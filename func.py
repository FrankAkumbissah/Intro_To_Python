def join_strings():
    sen = []
#loop to input and append the words to elements of the list
    n = int(input("enter the number of elements \n"))
    for i in range(0, n):
        ele = (input())
        sen.append(ele)
#loop to display the words in a list as a sentence
    for i in range(0, n):
        print(sen[i], end=" ")
        print(sen[i].upper(), end = " ")
    
join_strings()