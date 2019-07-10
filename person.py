def get_age():
    years = int(input("How old are you? \n"))
    return years

def get_name():
    name = input("What is your name? \n")
    return name
def main():
    print("Your name is", get_name(), "and you are", get_age(), "years old")
    
main()