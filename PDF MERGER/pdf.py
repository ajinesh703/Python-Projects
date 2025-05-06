import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

def select_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF files", "*.pdf")])
    if files:
        file_list.delete(0, tk.END)
        for f in files:
            file_list.insert(tk.END, f)

def merge_pdfs():
    files = file_list.get(0, tk.END)
    if not files:
        messagebox.showwarning("No Files", "Please select PDF files first.")
        return

    merger = PdfMerger()

    try:
        for pdf in files:
            merger.append(pdf)

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save Merged PDF As")

        if output_path:
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved at:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_list():
    file_list.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")
root.resizable(False, False)

title_label = tk.Label(root, text="📄 PDF Merger Tool", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

file_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=70, height=10)
file_list.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

select_btn = tk.Button(btn_frame, text="Select PDFs", width=15, command=select_files)
select_btn.grid(row=0, column=0, padx=5)

merge_btn = tk.Button(btn_frame, text="Merge PDFs", width=15, command=merge_pdfs)
merge_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear List", width=15, command=clear_list)
clear_btn.grid(row=0, column=2, padx=5)

footer = tk.Label(root, text="Developed by Ajinesh | PyPDF2 + Tkinter", font=("Arial", 10), fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
