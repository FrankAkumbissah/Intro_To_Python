from datetime import date

'''class person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def speak():
        print("Hello")
        
    def walk():
        print("Walking away")
        
    def get_name():
        print("My name is: ",self.name)
    
    def get_age():
        age = self.age'''
def calculateAge(birthDate):
    today = date.today()
    return = today.year - birthDate.year- ((today.month, today.day) < (birthDate.month, birthDate.day))
    print(calculateAge(1997, 2, 3), "years")