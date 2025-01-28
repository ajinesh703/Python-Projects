import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class BranchPredictionVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Branch Prediction Visualizer")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="Branch Prediction Visualizer", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Instruction input
        self.instruction_entry = ttk.Entry(self.root, width=50)
        self.instruction_entry.pack(pady=5)
        self.instruction_entry.insert(0, "Enter branch outcomes (e.g., T T N T N T T)")

        # Buttons
        simulate_button = ttk.Button(self.root, text="Simulate", command=self.simulate_prediction)
        simulate_button.pack(pady=5)

        # Prediction Method Selection
        method_label = ttk.Label(self.root, text="Select Prediction Method:", font=("Arial", 12))
        method_label.pack(pady=5)
        
        self.method_var = tk.StringVar(value="1-bit Predictor")
        methods = ["1-bit Predictor", "2-bit Predictor"]
        for method in methods:
            rb = ttk.Radiobutton(self.root, text=method, variable=self.method_var, value=method)
            rb.pack(anchor="w")

        # Graph Frame
        self.graph_frame = ttk.LabelFrame(self.root, text="Prediction Accuracy", padding=10)
        self.graph_frame.pack(pady=10, fill="both", expand=True)

    def simulate_prediction(self):
        outcomes = self.instruction_entry.get().strip().split()
        if not outcomes:
            return

        method = self.method_var.get()
        if method == "1-bit Predictor":
            accuracy = self.simulate_1bit_predictor(outcomes)
        else:
            accuracy = self.simulate_2bit_predictor(outcomes)

        self.plot_graph(outcomes, accuracy)

    def simulate_1bit_predictor(self, outcomes):
        correct_predictions = 0
        total_predictions = len(outcomes)
        predictor = "T"  # Initial prediction

        for outcome in outcomes:
            if outcome == predictor:
                correct_predictions += 1
            predictor = outcome  # Update predictor to the last outcome

        accuracy = correct_predictions / total_predictions
        return accuracy

    def simulate_2bit_predictor(self, outcomes):
        correct_predictions = 0
        total_predictions = len(outcomes)
        state = "Strongly Taken"  # Initial state

        state_machine = {
            "Strongly Taken": {"T": "Strongly Taken", "N": "Weakly Taken"},
            "Weakly Taken": {"T": "Strongly Taken", "N": "Weakly Not Taken"},
            "Weakly Not Taken": {"T": "Weakly Taken", "N": "Strongly Not Taken"},
            "Strongly Not Taken": {"T": "Weakly Not Taken", "N": "Strongly Not Taken"},
        }

        prediction_map = {
            "Strongly Taken": "T",
            "Weakly Taken": "T",
            "Weakly Not Taken": "N",
            "Strongly Not Taken": "N",
        }

        for outcome in outcomes:
            prediction = prediction_map[state]
            if outcome == prediction:
                correct_predictions += 1
            state = state_machine[state][outcome]  # Update state based on actual outcome

        accuracy = correct_predictions / total_predictions
        return accuracy

    def plot_graph(self, outcomes, accuracy):
        fig, ax = plt.subplots()
        x = list(range(1, len(outcomes) + 1))
        y = [random.uniform(0.8, 1.0) if outcome == "T" else random.uniform(0.5, 0.7) for outcome in outcomes]

        ax.plot(x, y, label="Prediction Confidence", marker="o")
        ax.set_title(f"Branch Prediction Accuracy: {accuracy * 100:.2f}%")
        ax.set_xlabel("Instruction Number")
        ax.set_ylabel("Prediction Confidence")
        ax.legend()

        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = BranchPredictionVisualizer(root)
    root.geometry("800x600")
    root.mainloop()
