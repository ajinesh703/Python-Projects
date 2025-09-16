import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

class AlgorithmVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")
        self.root.geometry("700x500")

        self.code_input = scrolledtext.ScrolledText(root, height=10)
        self.code_input.pack(fill=tk.X, padx=10, pady=5)
        self.code_input.insert(tk.END, "def run_algorithm():\n    arr = [5, 3, 8, 1]\n    for i in range(len(arr)):\n        for j in range(len(arr)-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n            visualize(arr)\n")

        self.run_button = tk.Button(root, text="Run", command=self.run_algorithm_thread)
        self.run_button.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(root, height=15, state='disabled')
        self.output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def visualize(self, state):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, f"{state}\n")
        self.output_area.yview(tk.END)
        self.output_area.config(state='disabled')
        self.root.update()

    def run_algorithm_thread(self):
        code = self.code_input.get("1.0", tk.END)
        thread = threading.Thread(target=self.run_algorithm, args=(code,))
        thread.start()

    def run_algorithm(self, code):
        # Provide a custom 'visualize' function to user code
        local_vars = {"visualize": self.visualize}
        try:
            exec(code, {}, local_vars)
            if "run_algorithm" in local_vars:
                local_vars["run_algorithm"]()
            else:
                messagebox.showerror("Error", "Define a function named run_algorithm().")
        except Exception as e:
            messagebox.showerror("Execution Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()
