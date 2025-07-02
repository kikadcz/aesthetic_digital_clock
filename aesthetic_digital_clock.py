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
        
    def _create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=800, height=320, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.cavas.configure(bg=self._bg_color)

    def _draw_strategic_dots(self):
        spacing = 60
        width = 800
        height = 320

        for x in range(0, width, spacing):
            for y in range(0, height, spacing):

                in_upper_left = x < width * 0.35 and y < height * 035
                in_lower_right = x > width * 0.65 and y > height * 0.65

                if in_upper_left or in_lower_right:
                    size = random.choice([15, 25, 35, 45])
                    offset = size // 2

                    color = random.choice(self._dot_colors)

                    self.canvas.create_oval(
                        x - offset, y - offset, x + offset, y + offset,
                        fill=color, outline=""
                    )

    def _create_widgets(self):
        self.label = tk.Label(
            self.canvas,
            font=self._font,
            bg=self._bg_color,
            fg=self._fg_color
        )
        self.canvas.create_window(400, 160, window=self.label)

        self.button_frame = tk.Frame(self.canvas, bg=self._bg_color)
        self.button_24hr = tk.Button(
            self.button_frame,
            text="24-Hour"
            font=("Helvetica", 12, "bold")
            fg=self._fg_color,
            padx=15
            pady=7,
            command=lambda: self._set_format("24-Hour")
        )
        self.button_24hr.pack(side="left", padx=10)


            self.button_frame = tk.Frame(self.canvas, bg=self._bg_color)
            self.button_12hr = tk.Button(
            self.button_frame,
            text="12-Hour"
            font = ("Helvetica", 12, "bold")
            fg = self._fg_color,
            padx = 15
            pady = 7,
            command = lambda: self._set_format("24-Hour")
        )
        self.button_12hr.pack(side="left", padx=10)

        self.canvas.create_window(400, 40, window=self.button_frame)
