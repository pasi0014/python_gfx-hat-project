import math
import random
import time
from gfxhat import lcd, backlight

# this function calculates the MPG, User is supposed to enter following values:
# - Miles 
# - Gallons
# Function returns value of calculated MPG
def calculateMPG(miles, gallons):
    totalMPG=miles/gallons
    return totalMPG
# This function calculates the area of the circle, User need to enter radius of the circle to get result.
# Function returns the calculated value of the area of the circle.
#
def calculateAreaOfCircle(radius):
    area=radius**2*math.pi
    return area
# This function converts Fahrenheit degrees into Celsium 
# User is expected to enter Fahrenheit degress to get result
# Function returns coverted degrees
def convertFahrenheitToCelsius(fahrenheit):
    celsium = (fahrenheit-32)*5/9
    return celsium

# This function will ask User to enter coordinates x,x1,y,y1
# Then it will use Pythagorean formula to calculate the distance between coordinates and then will return the result
# User is expected to enter all the coordinates
def calculateDistanceBetweenPoints(x,y,x1,y1):
    distance = math.sqrt( ( (x1-x)**2)  + ( (y1-y)**2) )
    return distance

# TASK 1
# This function draws the line on GFX hat by the given X coordinate.
# User need to enter the X coordinate to get the result on GFX hat.
def displVertLineAtX(x):
    lcd.clear()
    lcd.show()
    y=0
    while(y<=64):
        lcd.set_pixel(x,y,1)
        y=y+1
        lcd.show()
      

# TASK 2
# This function draws the line on GFX hat by the given Y coordinate
# User need to enter the Y coordinate to get the result on GFX hat.
def dispHorizLineAtY(y):
    lcd.clear()
    lcd.show()
    x=0
    while(x<=127):
        lcd.set_pixel(x,y,1)
        x=x+1
        lcd.show()

# TASK 3
# This function sets and displays pixels for one staircase with given width 
# and heaight 
def staircase(x,y,w=10,h=10):
    for i in range(w):
        if x+i<=127:
            lcd.set_pixel(x+i,y-h,1)
            lcd.show()
        else:
            h=i
    for j in range(h):
        if y>=0:
            lcd.set_pixel(x,y-j,1)
            lcd.show()
        else:
            w=j
    return(x+w,y-h)
# This function loops the previous function to dispaly staircase on the LCD screen
def showStaircase(x=0,y=63,w=10,h=10):
    lcd.clear()
    lcd.show()
    while(x+w<=127 and y-h>0):
        x,y=staircase(x,y,w,h)
    lcd.show()

# TASK 4
# this function set random coordinate for x and y. After that function supposed to display result at gfxhat.
def randomPixel(x,y): 
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(0.3)
    return(x,y)

# This function resets backlight color
def backlightColor():
    lcd.clear()
    lcd.show()
    backlight.set_all(100,100,100)
    backlight.show()
    
 # function displays given object on gfx hat   
def displayObject(obj,coordinateX,coordinateY):

    x = coordinateX 
    y = coordinateY

    if ( (coordinateX + len(obj[0])) > 127 ):
        coordinateX = 127 - len(obj[0])
    
    if ( coordinateY + len(obj) > 62 ):
        y = 63 - len(obj)

    for i in obj:
        y = y + 1
        x = coordinateX

        for j in i:
            x = x + 1
            lcd.set_pixel( x, y, j )
        lcd.show()
    
def menu():
    print("***************************")
    print("*   1. draw x line        *")
    print("*   2. draw y line        *")
    print("*   3. draw staircase     *")
    print("*   4. draw random pixel  *")
    print("*   5. reset backlight    *")
    print("*   6. display object     *")
    print("***************************")
    
    