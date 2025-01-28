import tkinter as tk
from tkinter import ttk

class CPUSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Instruction Simulator")
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        title_label = ttk.Label(self.root, text="CPU Instruction Simulator", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Instruction input
        self.instruction_entry = ttk.Entry(self.root, width=50)
        self.instruction_entry.pack(pady=5)
        self.instruction_entry.insert(0, "Enter Instruction (e.g., ADD R1, R2, R3)")

        # Buttons to execute simulation
        self.simulate_button = ttk.Button(self.root, text="Simulate", command=self.simulate_instruction)
        self.simulate_button.pack(pady=5)

        # Pipeline stages visualization
        self.pipeline_frame = ttk.LabelFrame(self.root, text="Pipeline Stages", padding=10)
        self.pipeline_frame.pack(pady=10, fill="x")

        stages = ["Fetch", "Decode", "Execute", "Memory", "Write Back"]
        self.stage_labels = {}
        for stage in stages:
            label = ttk.Label(self.pipeline_frame, text=f"{stage}: Idle", relief="ridge", padding=5)
            label.pack(side="left", expand=True, fill="x", padx=5)
            self.stage_labels[stage] = label

        # Output area
        self.output_text = tk.Text(self.root, height=10, wrap="word")
        self.output_text.pack(pady=10, fill="both", expand=True)
        self.output_text.insert("1.0", "Simulation output will be displayed here.")

    def simulate_instruction(self):
        instruction = self.instruction_entry.get().strip()
        if not instruction:
            self.output_text.insert("end", "\nError: Please enter a valid instruction.")
            return

        # Reset stages
        for stage in self.stage_labels:
            self.stage_labels[stage]["text"] = f"{stage}: Idle"

        # Simulate stages step-by-step
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", f"Simulating instruction: {instruction}\n")
        stages = ["Fetch", "Decode", "Execute", "Memory", "Write Back"]

        def update_stage(stage_idx):
            if stage_idx < len(stages):
                for i, stage in enumerate(stages):
                    if i == stage_idx:
                        self.stage_labels[stage]["text"] = f"{stage}: Active"
                    else:
                        self.stage_labels[stage]["text"] = f"{stage}: Completed" if i < stage_idx else f"{stage}: Idle"

                # Log to output
                self.output_text.insert("end", f"{stages[stage_idx]} stage completed.\n")
                self.root.after(1000, lambda: update_stage(stage_idx + 1))

        update_stage(0)

if __name__ == "__main__":
    root = tk.Tk()
    simulator = CPUSimulator(root)
    root.geometry("600x400")
    root.mainloop()
