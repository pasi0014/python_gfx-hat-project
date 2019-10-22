from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
import click
import pasi0014 as p
backlight.set_all(255,255,255)
backlight.show()
lcd.clear()
lcd.show()
def clearScreen(lcd):
    lcd.clear()
    lcd.show()
#Displays text on the gfx hat
def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 
displayText("Etch a skretch",lcd,x=20,y=30)





#Etch a Sketch game

r = ''
x=0
y=0

while (r != 'q'):
    r=click.getchar()
    
    if ( r == '\x1b[A'):
        y=y-1
        if(y<0):
            y=63
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif ( r == '\x1b[B'):
        y=y+1
        if (y>63):
            y=0
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif ( r == '\x1b[C'):
        x=x+1
        if(x>127):
            x=0
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif ( r == '\x1b[D'):
        x=x-1
        if (x<0):
            x=127
        lcd.set_pixel(x,y,1)
        lcd.show()
    elif( r == 's'):
        clearScreen(lcd)
    elif( r == 'q'):
        clearScreen(lcd)
        
        
            
        


