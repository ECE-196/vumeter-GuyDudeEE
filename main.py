import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39


    # type: ignore
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

def set_leds(volume, num_lit_leds):
    for i in range(len(leds)):
        leds[i].value = (i < num_lit_leds)

# Main loop
while True:
    volume = microphone.value
    static = 20000
    max_range = 28000
    volume_per_led = (max_range / len(leds))
    num_lit_leds = min(int((volume-static) / volume_per_led), len(leds))
    set_leds(volume, num_lit_leds)
    #print(volume)
    #sleep(.1)
