from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
from gpiozero import Button
import signal
#activate virtual env with source ~/.virtualenvs/pimoroni/bin/activate

inky_display = auto()

BUTTONS = [5, 6, 16]
LABELS = ["/home/raspberry/LearnerPlateEInk/L.jpg", "/home/raspberry/LearnerPlateEInk/RedP.jpg", "/home/raspberry/LearnerPlateEInk/GreenP.jpg"]

def display_image(filepath):
    img = Image.open(filepath)
    img = img.rotate(-90, expand=True)
    inky_display.set_image(img)
    inky_display.show()

def handle_button(pin):
    fileName = LABELS[BUTTONS.index(pin.pin.number)]
    print(f"button press detected on pin {pin}")
    display_image(fileName)

for pin in BUTTONS:
    button = Button(pin=pin, pull_up=True, bounce_time=0.1)
    button.when_pressed = handle_button
    

signal.pause()                   
