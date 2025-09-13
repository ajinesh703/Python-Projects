"""
Algorithm Visualizer Example
This is a working example of Bubble Sort visualization.
Run: python this_file.py
"""

import tkinter as tk
import random
from typing import Generator, Dict, List

def bubble_sort(arr: List[int]) -> Generator[Dict, None, None]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            yield {'array': a[:], 'i': j, 'j': j+1, 'action': 'compare'}
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                yield {'array': a[:], 'i': j, 'j': j+1, 'action': 'swap'}
    yield {'array': a[:], 'i': None, 'j': None, 'action': 'done'}

class Visualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bubble Sort Visualizer Example")
        self.geometry("800x500")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.array = [random.randint(10, 400) for _ in range(30)]
        self.generator = bubble_sort(self.array)
        self.after(50, self.step)

    def draw_array(self, state):
        self.canvas.delete("all")
        bar_width = 800 // len(state['array'])
        for idx, val in enumerate(state['array']):
            x0 = idx * bar_width
            x1 = x0 + bar_width - 2
            y0 = 500 - val
            y1 = 500
            color = "#4da6ff"
            if state['action'] == 'compare' and idx in [state['i'], state['j']]:
                color = "#ffcc00"
            elif state['action'] == 'swap' and idx in [state['i'], state['j']]:
                color = "#ff4444"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def step(self):
        try:
            state = next(self.generator)
            self.draw_array(state)
            self.after(50, self.step)
        except StopIteration:
            return

if __name__ == "__main__":
    app = Visualizer()
    app.mainloop()
