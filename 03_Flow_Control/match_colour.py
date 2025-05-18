"""
While traveling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
------

`match` is a new operator introduced in Python 3.10
"""

fav_color: str = input("Enter your favorite color: ").lower()

match fav_color:
    case "black":
        print("Louis has a BLACK T-Shirt.")
    case "red":
        print("Louis has a RED car.")
    case "yellow":
        print("Louis has YELLOW shoes.")
    case "green":
        print("Louis has a GREEN hat")
    case _:
        print(f"Louis has nothing in {fav_color} color.")
import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
times= n
x, y = [int(i) for i in input().split()]
if not (w>=1 and w<10000):
    raise ValueError(f"w {w} incorrect!")
if not (h>=1 and h<10000):
    raise ValueError(f"h {h} incorrect!")
if not (n>=2 and n<100):
    raise ValueError(f"n {n} incorrect!")
if not (x<w):
    raise ValueError("x0<w incorrect!")
if not (y<h):
    raise ValueError("y0<h incorrect!")


directions = {
    "U" : (0,-1,0), # ok
    "UR" : (1,-1,1), #OK
    "R" : (1,0,2), #OK
    "DR" : (1,1,3), #OK
    "D" : (0,1,4), #OK
    "DL" : (-1,1,5), #OK
    "L" : (-1,0,6), #OK
    "UL" : (-1,-1,7),
}
x_min = 0
x_max= w-1
y_min = 0
y_max = h-1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    a,b,direct= directions[bomb_dir]


    if direct == 0:
        y_max = y
        y = y_max -  int((y_max - y_min)/2)
        if y==y_max and y<y_min:
            y=y-1
    elif direct == 1 :
        x_min = x
        y_max = y
        x = x_min + int((x_max - x_min )/2)
        if x==x_min and x<x_max:
            x=x+1
        y = y_max -  int((y_max - y_min)/2)
        if y==y_max and y<y_min:
            y=y-1
    elif direct == 2:
        x_min = x
        x = x_min + int((x_max - x_min )/2)
        if x==x_min and x<x_max:
            x=x+1
    elif direct == 3:
        x_min = x
        y_min = y
        x = x_min+int((x_max - x_min)/2)
        if x<x_max and x==x_min:
            x=x+1
        y = y_min + int((y_max - y_min)/2)
        if y<y_max and y==y_min:
            y=y+1
    elif direct == 4:
        y_min = y
        y= y_min + int((y_max-y_min)/2)
        if y<y_max and y==y_min:
            y=y+1
    elif direct == 5:
        x_max = x
        y_min = y
        x= x_max - int((x_max-x_min)/2)
        if x==x_max and x<x_min:
            x=x-1
        y= y_min + int((y_max-y_min)/2)
        if y<y_max and y==y_min:
            y=y+1
    elif direct == 6:
        x_max = x
        x= x_max - int((x_max-x_min)/2)
        if x==x_max and x<x_min:
            x=x-1
    elif direct == 7:
        x_max = x
        y_max = y
        if x != 0:
            x= x_max - int((x_max-x_min)/2)
            if x==x_max and x>x_min:
                x=x-1
        if y != 0:

            y = y_max -  int((y_max - y_min)/2)
            if y==y_max and y>y_min:
                y=y-1

    # the location of the next window Batman should jump to.
    if (x<0 or x>w-1 ) or (y<0 and y>h-1 ):
        raise ValueError("bomb_dir incorrect")
    print(f"{x} {y}")
    n-=1
