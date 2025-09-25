import machine
import neopixel
import time

pin = 5
num_leds = 1
np = neopixel.NeoPixel(machine.Pin(pin), num_leds)

while True:
    # התחזקות הדרגתית
    for brightness in range(0, 256, 5):
        np[0] = (brightness, brightness, brightness)
        np.write()
        time.sleep(10)  # המתנה של 10 שניות

    # היחלשות הדרגתית
    for brightness in range(255, -1, -5):
        np[0] = (brightness, brightness, brightness)
        np.write()
        time.sleep(10)  # המתנה של 10 שניות
