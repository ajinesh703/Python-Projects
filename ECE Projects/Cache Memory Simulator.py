import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CacheSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cache Memory Simulator")
        self.create_widgets()

        self.cache_size = 4
        self.block_size = 1
        self.memory_blocks = [i for i in range(16)]  # Simulated main memory (16 blocks)
        self.cache = []
        self.replacement_policy = "LRU"
        self.mapping_technique = "Direct Mapping"

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="Cache Memory Simulator", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Cache Configuration
        config_frame = ttk.LabelFrame(self.root, text="Configuration", padding=10)
        config_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(config_frame, text="Cache Size:").grid(row=0, column=0, padx=5, pady=5)
        self.cache_size_entry = ttk.Entry(config_frame, width=10)
        self.cache_size_entry.insert(0, "4")
        self.cache_size_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(config_frame, text="Block Size:").grid(row=1, column=0, padx=5, pady=5)
        self.block_size_entry = ttk.Entry(config_frame, width=10)
        self.block_size_entry.insert(0, "1")
        self.block_size_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(config_frame, text="Mapping Technique:").grid(row=2, column=0, padx=5, pady=5)
        self.mapping_combo = ttk.Combobox(config_frame, values=["Direct Mapping", "Associative Mapping", "Set-Associative Mapping"], state="readonly")
        self.mapping_combo.current(0)
        self.mapping_combo.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(config_frame, text="Replacement Policy:").grid(row=3, column=0, padx=5, pady=5)
        self.replacement_combo = ttk.Combobox(config_frame, values=["LRU", "FIFO"], state="readonly")
        self.replacement_combo.current(0)
        self.replacement_combo.grid(row=3, column=1, padx=5, pady=5)

        apply_button = ttk.Button(config_frame, text="Apply", command=self.apply_configuration)
        apply_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Memory Access
        access_frame = ttk.LabelFrame(self.root, text="Memory Access", padding=10)
        access_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(access_frame, text="Access Block:").grid(row=0, column=0, padx=5, pady=5)
        self.access_entry = ttk.Entry(access_frame, width=10)
        self.access_entry.grid(row=0, column=1, padx=5, pady=5)

        access_button = ttk.Button(access_frame, text="Access", command=self.access_memory)
        access_button.grid(row=0, column=2, padx=5, pady=5)

        # Visualization
        self.result_frame = ttk.LabelFrame(self.root, text="Simulation Results", padding=10)
        self.result_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.result_text = tk.Text(self.result_frame, height=15, wrap="word")
        self.result_text.pack(fill="both", expand=True)

    def apply_configuration(self):
        try:
            self.cache_size = int(self.cache_size_entry.get())
            self.block_size = int(self.block_size_entry.get())
            self.mapping_technique = self.mapping_combo.get()
            self.replacement_policy = self.replacement_combo.get()

            self.cache = []
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Configuration applied:\nCache Size: {self.cache_size}\nBlock Size: {self.block_size}\nMapping Technique: {self.mapping_technique}\nReplacement Policy: {self.replacement_policy}\n")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for cache and block size.")

    def access_memory(self):
        try:
            block = int(self.access_entry.get())
            if block not in self.memory_blocks:
                raise ValueError("Invalid block number.")

            if self.mapping_technique == "Direct Mapping":
                self.direct_mapping(block)
            elif self.mapping_technique == "Associative Mapping":
                self.associative_mapping(block)
            elif self.mapping_technique == "Set-Associative Mapping":
                self.set_associative_mapping(block)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def direct_mapping(self, block):
        index = block % self.cache_size

        if len(self.cache) <= index or self.cache[index] != block:
            if len(self.cache) > index:
                self.cache[index] = block
            else:
                self.cache.append(block)
            self.result_text.insert(tk.END, f"Cache Miss: Block {block} loaded at index {index}.\n")
        else:
            self.result_text.insert(tk.END, f"Cache Hit: Block {block} found at index {index}.\n")

    def associative_mapping(self, block):
        if block in self.cache:
            self.result_text.insert(tk.END, f"Cache Hit: Block {block} found.\n")
        else:
            if len(self.cache) < self.cache_size:
                self.cache.append(block)
            else:
                self.replace_block(block)
            self.result_text.insert(tk.END, f"Cache Miss: Block {block} loaded into cache.\n")

    def set_associative_mapping(self, block):
        # Simple 2-way set associative mapping
        set_index = block % (self.cache_size // 2)
        if len(self.cache) <= set_index * 2 or block not in self.cache[set_index * 2: set_index * 2 + 2]:
            if len(self.cache) > set_index * 2 + 1:
                self.cache[set_index * 2 + 1] = block
            elif len(self.cache) > set_index * 2:
                self.cache[set_index * 2] = block
            else:
                self.cache.extend([block] * 2)
            self.result_text.insert(tk.END, f"Cache Miss: Block {block} loaded in set {set_index}.\n")
        else:
            self.result_text.insert(tk.END, f"Cache Hit: Block {block} found in set {set_index}.\n")

    def replace_block(self, block):
        if self.replacement_policy == "LRU":
            self.cache.pop(0)
        elif self.replacement_policy == "FIFO":
            self.cache.pop(0)
        self.cache.append(block)

if __name__ == "__main__":
    root = tk.Tk()
    app = CacheSimulator(root)
    root.geometry("800x600")
    root.mainloop()
