#!/usr/bin/env python3
"""
PDF Merger - A modern GUI application for merging PDF files
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from pypdf import PdfWriter, PdfReader
import sys
from typing import List


class ModernPDFMerger:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Pro")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)
        
        # Modern color scheme
        self.colors = {
            'bg': '#1e1e2e',
            'surface': '#2a2a3e',
            'surface_light': '#363650',
            'primary': '#6366f1',
            'primary_hover': '#4f46e5',
            'success': '#22c55e',
            'danger': '#ef4444',
            'text': '#e5e5e5',
            'text_dim': '#a0a0a0',
            'border': '#404055'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # PDF files list
        self.pdf_files: List[str] = []
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_container, bg=self.colors['bg'])
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            header_frame,
            text="📄 PDF Merger Pro",
            font=('Segoe UI', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        title_label.pack(side=tk.LEFT)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Combine multiple PDFs into one",
            font=('Segoe UI', 11),
            bg=self.colors['bg'],
            fg=self.colors['text_dim']
        )
        subtitle_label.pack(side=tk.LEFT, padx=(15, 0))
        
        # File list section
        list_frame = tk.Frame(main_container, bg=self.colors['surface'], relief=tk.FLAT, bd=0)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # List header
        list_header = tk.Frame(list_frame, bg=self.colors['surface'])
        list_header.pack(fill=tk.X, padx=15, pady=(15, 10))
        
        list_title = tk.Label(
            list_header,
            text="PDF Files",
            font=('Segoe UI', 12, 'bold'),
            bg=self.colors['surface'],
            fg=self.colors['text']
        )
        list_title.pack(side=tk.LEFT)
        
        count_label_frame = tk.Frame(list_header, bg=self.colors['surface_light'], bd=0)
        count_label_frame.pack(side=tk.LEFT, padx=(10, 0))
        
        self.count_label = tk.Label(
            count_label_frame,
            text="0 files",
            font=('Segoe UI', 10),
            bg=self.colors['surface_light'],
            fg=self.colors['text_dim'],
            padx=8,
            pady=2
        )
        self.count_label.pack()
        
        # Listbox with scrollbar
        listbox_container = tk.Frame(list_frame, bg=self.colors['surface'])
        listbox_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        scrollbar = tk.Scrollbar(listbox_container, bg=self.colors['surface'])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(
            listbox_container,
            font=('Consolas', 10),
            bg=self.colors['surface_light'],
            fg=self.colors['text'],
            selectbackground=self.colors['primary'],
            selectforeground='white',
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightbackground=self.colors['border'],
            highlightcolor=self.colors['primary'],
            yscrollcommand=scrollbar.set
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # Button panel
        button_panel = tk.Frame(main_container, bg=self.colors['bg'])
        button_panel.pack(fill=tk.X)
        
        # Left side buttons
        left_buttons = tk.Frame(button_panel, bg=self.colors['bg'])
        left_buttons.pack(side=tk.LEFT)
        
        self.add_button = self.create_button(
            left_buttons,
            "➕ Add PDFs",
            self.add_files,
            bg=self.colors['primary']
        )
        self.add_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.remove_button = self.create_button(
            left_buttons,
            "🗑️ Remove",
            self.remove_selected,
            bg=self.colors['danger']
        )
        self.remove_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_button = self.create_button(
            left_buttons,
            "Clear All",
            self.clear_all,
            bg=self.colors['surface_light']
        )
        self.clear_button.pack(side=tk.LEFT)
        
        # Right side buttons
        right_buttons = tk.Frame(button_panel, bg=self.colors['bg'])
        right_buttons.pack(side=tk.RIGHT)
        
        self.move_up_button = self.create_button(
            right_buttons,
            "⬆️",
            self.move_up,
            bg=self.colors['surface_light'],
            width=5
        )
        self.move_up_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.move_down_button = self.create_button(
            right_buttons,
            "⬇️",
            self.move_down,
            bg=self.colors['surface_light'],
            width=5
        )
        self.move_down_button.pack(side=tk.LEFT, padx=(0, 15))
        
        self.merge_button = self.create_button(
            right_buttons,
            "✨ Merge PDFs",
            self.merge_pdfs,
            bg=self.colors['success'],
            width=15
        )
        self.merge_button.pack(side=tk.LEFT)
        
        # Status bar
        status_frame = tk.Frame(main_container, bg=self.colors['surface'], height=40, relief=tk.FLAT, bd=0)
        status_frame.pack(fill=tk.X, pady=(15, 0))
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready to merge PDFs",
            font=('Segoe UI', 10),
            bg=self.colors['surface'],
            fg=self.colors['text_dim'],
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.BOTH, padx=15, pady=10)
        
    def create_button(self, parent, text, command, bg, width=None):
        """Create a styled button"""
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=('Segoe UI', 10, 'bold'),
            bg=bg,
            fg='white',
            activebackground=self.colors['primary_hover'] if bg == self.colors['primary'] else bg,
            activeforeground='white',
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        
        if width:
            button.config(width=width)
        
        # Hover effects
        def on_enter(e):
            if bg == self.colors['primary']:
                button.config(bg=self.colors['primary_hover'])
            else:
                button.config(bg=self.lighten_color(bg))
                
        def on_leave(e):
            button.config(bg=bg)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
    
    def lighten_color(self, hex_color):
        """Lighten a hex color"""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, r + 20)
        g = min(255, g + 20)
        b = min(255, b + 20)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def add_files(self):
        """Add PDF files to the list"""
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
                    filename = Path(file).name
                    self.listbox.insert(tk.END, f"  {filename}")
            
            self.update_count()
            self.update_status(f"Added {len(files)} file(s)")
    
    def remove_selected(self):
        """Remove selected file from the list"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)
            del self.pdf_files[index]
            self.update_count()
            self.update_status("Removed file")
        else:
            messagebox.showwarning("No Selection", "Please select a file to remove")
    
    def clear_all(self):
        """Clear all files from the list"""
        if self.pdf_files:
            if messagebox.askyesno("Clear All", "Remove all files from the list?"):
                self.listbox.delete(0, tk.END)
                self.pdf_files.clear()
                self.update_count()
                self.update_status("Cleared all files")
    
    def move_up(self):
        """Move selected file up in the list"""
        selection = self.listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        if index > 0:
            # Swap in list
            self.pdf_files[index], self.pdf_files[index-1] = \
                self.pdf_files[index-1], self.pdf_files[index]
            
            # Update listbox
            item = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index-1, item)
            self.listbox.selection_set(index-1)
    
    def move_down(self):
        """Move selected file down in the list"""
        selection = self.listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        if index < len(self.pdf_files) - 1:
            # Swap in list
            self.pdf_files[index], self.pdf_files[index+1] = \
                self.pdf_files[index+1], self.pdf_files[index]
            
            # Update listbox
            item = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index+1, item)
            self.listbox.selection_set(index+1)
    
    def merge_pdfs(self):
        """Merge all PDFs in the list"""
        if not self.pdf_files:
            messagebox.showwarning("No Files", "Please add PDF files to merge")
            return
        
        if len(self.pdf_files) < 2:
            messagebox.showwarning("Not Enough Files", "Please add at least 2 PDF files to merge")
            return
        
        # Ask for output file
        output_file = filedialog.asksaveasfilename(
            title="Save merged PDF as",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        
        if not output_file:
            return
        
        try:
            self.update_status("Merging PDFs...")
            self.root.update()
            
            writer = PdfWriter()
            total_pages = 0
            
            for pdf_file in self.pdf_files:
                reader = PdfReader(pdf_file)
                for page in reader.pages:
                    writer.add_page(page)
                    total_pages += 1
            
            with open(output_file, "wb") as output:
                writer.write(output)
            
            self.update_status(f"✓ Successfully merged {len(self.pdf_files)} files ({total_pages} pages)")
            messagebox.showinfo(
                "Success",
                f"PDFs merged successfully!\n\n"
                f"Files merged: {len(self.pdf_files)}\n"
                f"Total pages: {total_pages}\n"
                f"Output: {Path(output_file).name}"
            )
            
        except Exception as e:
            self.update_status("✗ Error merging PDFs")
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")
    
    def update_count(self):
        """Update the file count label"""
        count = len(self.pdf_files)
        self.count_label.config(text=f"{count} file{'s' if count != 1 else ''}")
    
    def update_status(self, message):
        """Update the status bar"""
        self.status_label.config(text=message)


def main():
    """Main entry point"""
    # Check if pypdf is installed
    try:
        import pypdf
    except ImportError:
        print("Error: pypdf is not installed")
        print("Please install it using: pip install pypdf --break-system-packages")
        sys.exit(1)
    
    root = tk.Tk()
    app = ModernPDFMerger(root)
    root.mainloop()


if __name__ == "__main__":
    main()
