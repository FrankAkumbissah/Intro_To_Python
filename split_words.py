#splitting a sentence into words
def sen():
    sentence = input("please enter a sentence \n")
    split_sent = sentence.split(" ")
    print(split_sent)
    string = ""
    for i in split_sent:
        string = string + i + ", "
    print(string)
    

    
def main():
    sen()
    
main()    