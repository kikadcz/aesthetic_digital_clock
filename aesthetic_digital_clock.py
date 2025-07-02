import time
import tkinter as tk
import random
import colorsys

class PolClock;
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PolClock Dots")
        self.window.geometry("800x320")
        self.window.resizable(True, True)


        self._bg_color = '#E6F3FF'
        self._base_hue = random.uniform(0, 1)

        self._dot_colors = [self._generate_pastel_color(h)]
                          for h in [self._base_hue + i/6 for i in range(6)]]

        self._fg_color = '#2C3E50'
        self._font = ("Arial", 130, "bold")

        self.time_format = "24-Hour"

        self._create_canvas()
        self._draw_strategic_dots()
        self._create_widgets()
        self._update_time()

    def _generate_pastel_color(self, hue):
        saturation = 0.4
        value = 0.95
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        return f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb)[2]*255):02x}'
        
    
