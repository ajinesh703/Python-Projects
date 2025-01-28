import tkinter as tk
from tkinter import ttk

class ArchitectureComparisonTool:
    def __init__(self, root):
        self.root = root
        self.root.title("RISC vs. CISC Architecture Comparison Tool")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="RISC vs. CISC Architecture Comparison", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Instruction input
        self.instruction_entry = ttk.Entry(self.root, width=50)
        self.instruction_entry.pack(pady=5)
        self.instruction_entry.insert(0, "Enter a program (e.g., LOAD A, ADD B, STORE C)")

        # Simulate button
        simulate_button = ttk.Button(self.root, text="Simulate", command=self.simulate_comparison)
        simulate_button.pack(pady=5)

        # Comparison Frame
        self.comparison_frame = ttk.LabelFrame(self.root, text="Comparison Results", padding=10)
        self.comparison_frame.pack(pady=10, fill="x")

        # RISC and CISC Outputs
        self.risc_output = tk.Text(self.comparison_frame, height=10, wrap="word")
        self.risc_output.pack(side="left", fill="both", expand=True, padx=5)
        self.risc_output.insert("1.0", "RISC Architecture Output:\n")

        self.cisc_output = tk.Text(self.comparison_frame, height=10, wrap="word")
        self.cisc_output.pack(side="right", fill="both", expand=True, padx=5)
        self.cisc_output.insert("1.0", "CISC Architecture Output:\n")

        # Summary
        self.summary_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.summary_label.pack(pady=10)

    def simulate_comparison(self):
        program = self.instruction_entry.get().strip().upper()
        if not program:
            self.risc_output.insert("end", "\nError: No program entered.")
            self.cisc_output.insert("end", "\nError: No program entered.")
            return

        instructions = program.split(",")

        # Simulate RISC
        risc_clock_cycles = 0
        self.risc_output.delete("1.0", "end")
        self.risc_output.insert("1.0", "RISC Architecture Output:\n")
        for instr in instructions:
            risc_clock_cycles += 1  # Each instruction takes 1 cycle
            self.risc_output.insert("end", f"Executing: {instr.strip()} (1 cycle)\n")

        self.risc_output.insert("end", f"\nTotal Clock Cycles (RISC): {risc_clock_cycles}\n")

        # Simulate CISC
        cisc_clock_cycles = 0
        self.cisc_output.delete("1.0", "end")
        self.cisc_output.insert("1.0", "CISC Architecture Output:\n")
        for instr in instructions:
            if "LOAD" in instr or "STORE" in instr:
                cisc_clock_cycles += 2  # Load/Store takes 2 cycles
            else:
                cisc_clock_cycles += 1  # Other instructions take 1 cycle
            self.cisc_output.insert("end", f"Executing: {instr.strip()} ({'2 cycles' if 'LOAD' in instr or 'STORE' in instr else '1 cycle'})\n")

        self.cisc_output.insert("end", f"\nTotal Clock Cycles (CISC): {cisc_clock_cycles}\n")

        # Summary
        self.summary_label.config(text=f"RISC: {risc_clock_cycles} cycles | CISC: {cisc_clock_cycles} cycles")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArchitectureComparisonTool(root)
    root.geometry("800x600")
    root.mainloop()
