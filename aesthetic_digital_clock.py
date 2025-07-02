import time
import tkinter as tk
import random
import colorsys


class PolClock:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("PolClock Dots")
        self.main_window.geometry("800x320")
        self.main_window.resizable(True, True)

        # Enhanced pastel color palette
        self.background_color = "#E6F3FF"
        self.base_hue = random.uniform(0, 1)

        # Generate harmonious colors
        self.dot_colors = [self._generate_pastel_color(hue_value)
                           for hue_value in [self.base_hue + hue_offset / 6
                                             for hue_offset in range(6)]]

        self.foreground_color = "#2C3E50"
        self.clock_font = ("Arial", 130, "bold")

        self.time_format = "24-Hour"

        self._create_canvas()
        self._draw_strategic_dots()
        self._create_widgets()
        self._update_time()

    def _generate_pastel_color(self, hue_value):
        """Generate a soft pastel color based on hue"""
        saturation = 0.4
        value = 0.95
        rgb = colorsys.hsv_to_rgb(hue_value, saturation, value)
        return f'#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}'

    def _create_canvas(self):
        self.canvas = tk.Canvas(self.main_window, width=800, height=320, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.configure(bg=self.background_color)

    def _draw_strategic_dots(self):
        dot_spacing = 60
        canvas_width = 800
        canvas_height = 320

        for x_position in range(0, canvas_width, dot_spacing):
            for y_position in range(0, canvas_height, dot_spacing):
                # Improved dot placement logic
                in_upper_left = x_position < canvas_width * 0.35 and y_position < canvas_height * 0.35
                in_lower_right = x_position > canvas_width * 0.65 and y_position > canvas_height * 0.65

                if in_upper_left or in_lower_right:
                    # Enhanced dot properties
                    dot_size = random.choice([15, 25, 35, 45])
                    dot_offset = dot_size // 2

                    # Select random color from palette
                    dot_color = random.choice(self.dot_colors)

                    self.canvas.create_oval(
                        x_position - dot_offset, y_position - dot_offset,
                        x_position + dot_offset, y_position + dot_offset,
                        fill=dot_color, outline=""
                    )

    def _create_widgets(self):
        # Clock label with improved styling
        self.time_label = tk.Label(
            self.canvas,
            font=self.clock_font,
            bg=self.background_color,
            fg=self.foreground_color
        )
        self.canvas.create_window(400, 160, window=self.time_label)

        # Format buttons with enhanced appearance
        self.button_frame = tk.Frame(self.canvas, bg=self.background_color)
        self.hour24_button = tk.Button(
            self.button_frame,
            text="24-Hour",
            font=("Helvetica", 12, "bold"),
            bg="#B3D9FF",
            fg=self.foreground_color,
            padx=15,
            pady=7,
            command=lambda: self._set_format("24-Hour")
        )
        self.hour24_button.pack(side="left", padx=10)

        self.hour12_button = tk.Button(
            self.button_frame,
            text="12-Hour",
            font=("Helvetica", 12, "bold"),
            bg="#B3D9FF",
            fg=self.foreground_color,
            padx=15,
            pady=7,
            command=lambda: self._set_format("12-Hour")
        )
        self.hour12_button.pack(side="left", padx=10)

        self.canvas.create_window(400, 40, window=self.button_frame)

    def _set_format(self, format_type):
        self.time_format = format_type

    def _update_time(self):
        if self.time_format == "12-Hour":
            current_time = time.strftime("%I:%M:%S").lstrip("0")
        else:
            current_time = time.strftime("%H:%M:%S")

        self.time_label.config(text=current_time)
        self.time_label.after(500, self._update_time)

    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    my_clock = PolClock()
    my_clock.run()