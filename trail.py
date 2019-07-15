#i = 10
#while(i < 20):
 #   i = i + 2
  #  print (i)

def evens():
    start = int(input("Enter the start of the numbers: "))
    end = int(input("Enter the end of the numbers: "))
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num, end = " ")
            num2 = num
            num2 = str(num2)

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
        
def sent():
    text = input("Enter a string: ")
    if "a" in text:
        print("true")
    else:
        print("False")
    
def sent2():
    text = input("Enter a string: ")
    print(text.find("a"))
    
def letter_search3():
    text = input("Enter a string: ")
    if (text.count("s") != 0 and text.count("m") != 0):
        print("True")
    else:
        print("False")
        
def evens():
    frank = []
    n = int(input("enter the number of elements \n"))
    for i in range(0, n):
        ele = int(input())
        frank.append(ele)
    for i in range(0, n):
        print(frank[i], end=" ")
        
def main():
    distance()
    

def distance():
    first_city = input("Enter the first city: ")
    second_city = input("Enter the second city: ")
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my application")
    location = geolocator.geocode(first_city)
    print(first_city, "is found in: ",location.address)
    lat = location.latitude
    long = location.longitude

    location = geolocator.geocode(second_city)
    print(second_city, "is found in: ",location.address)
    lat2 = location.latitude
    long2 = location.longitude

    from geopy.distance import geodesic
    first = (long, lat)
    second = (long2, lat2)
    print(geodesic(first, second).miles)


    
main()