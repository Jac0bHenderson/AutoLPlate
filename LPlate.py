from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
from gpiozero import Button
import signal
#activate virtual env with source ~/.virtualenvs/pimoroni/bin/activate

print("Running L Plate Display")

try:
    inky_display = auto()

    print("Getting Image files")
    LPlate = Image.open("/home/pi/AutoLPlate/L.jpg").rotate(-90, expand=True)
    RedPPlate = Image.open("/home/pi/AutoLPlate/RedP.jpg").rotate(-90, expand=True)
    GreenPPlate = Image.open("/home/pi/AutoLPlate/GreenP.jpg").rotate(-90, expand=True)
    print("Images loaded")

    BUTTONS = {
        5 : LPlate, 
        6 : RedPPlate, 
        16 : GreenPPlate
    }

    def display_image(img):
        inky_display.set_image(img)
        inky_display.show()

    def handle_button(btn):
        pin_number = btn.pin.number
        print(f"button press detected on pin {pin_number}")
        display_image(BUTTONS[pin_number])

    for pin in BUTTONS.keys():
        button = Button(pin=pin, pull_up=True, bounce_time=0.1)
        button.when_pressed = handle_button
        
    signal.pause()              
except Exception as ex:
    print(ex)     
