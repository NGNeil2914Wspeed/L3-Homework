from time import sleep
from math import sqrt

def da_thing():
    sleep(1)
    print ("...")
    sleep(1)

def getint(question):
    while True:
        try:
            a = int(input(question))
            da_thing
            return a
        except ValueError as e:
            da_thing
            print (f"{e}\nError! Please enter a whole number.")
            da_thing

name = input("What\'s is your name? ")
da_thing
number = getint(f"Hey {name}, I\'m going to help you find the square root of any (whole) number so first, I\'m going to need that number so can you just enter it? ")
ans = sqrt(number)
print (f"The square root of your number ({number}) is {ans}")