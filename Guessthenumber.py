import random
import math
l=int(input("enter the lower limit:"))
u=int(input("enter the upper limit:"))
Range= list(range(l,u))
a=(random.choice(Range))




c=5
while c>=0:
    b = int(input("enter your guess"))
    if a == b:
        print("congratulations!!! you have guessed correctly!!!")
    elif a > b:
        print("your guess is smaller then the number")
    elif a < b:
        print("your guess is larger then the number")

    c=c-1

print("bad luck!! try again")
