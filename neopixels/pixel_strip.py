import time
from neopixel import *

from utils import colors


class PixelStrip:
    LED_COUNT = 60  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 5  # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

    def __init__(self):
        self.strip = Adafruit_NeoPixel(
            self.LED_COUNT,
            self.LED_PIN,
            self.LED_FREQ_HZ,
            self.LED_DMA,
            self.LED_INVERT,
            self.LED_BRIGHTNESS
        )
        self.strip.begin()
        self.pixels = map(lambda x: Pixel(x, colors.black), list(range(self.num_pixels())))

    def color_wipe(self, color, wait_ms=50):
        for i in range(self.num_pixels()):
            self.set_color_of(i, color)
            time.sleep(wait_ms / 1000.0)

    def num_pixels(self):
        return self.strip.numPixels()

    def set_color_of(self, pixel_index, color):
        self.strip.setPixelColor(pixel_index, color.to_i())
        self.strip.show()

    def reset(self):
        for i in range(self.num_pixels()):
            self.set_color_of(i, colors.black)


class Pixel:
    def __init__(self, index, color):
        self.index = index
        self.color = color

    def set_color(self, new_color):
        self.set_color(new_color)
