import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class NucleiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VCS Scanner")
        
        # Title label
        self.title_label = tk.Label(root, text="VCS Scanner", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        # Target URL input
        self.url_label = tk.Label(root, text="Target URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()
        
        # Template selection
        self.template_label = tk.Label(root, text="Nuclei Template:")
        self.template_label.pack()
        self.template_entry = tk.Entry(root, width=50)
        self.template_entry.pack()
        self.template_button = tk.Button(root, text="Select Template", command=self.select_template)
        self.template_button.pack()
        
        # Start scan button
        self.scan_button = tk.Button(root, text="Start Scan", command=self.start_scan)
        self.scan_button.pack(pady=10)
        
        # Output text area
        self.output_text = tk.Text(root, height=20, width=80)
        self.output_text.pack(pady=10)
        
    def select_template(self):
        template_path = filedialog.askopenfilename(title="Select Nuclei Template", filetypes=[("YAML files", "*.yaml")])
        if template_path:
            self.template_entry.delete(0, tk.END)
            self.template_entry.insert(0, template_path)
    
    def start_scan(self):
        target_url = self.url_entry.get()
        template_path = self.template_entry.get()
        
        if not target_url or not template_path:
            messagebox.showwarning("Input Error", "Please provide both target URL and template path.")
            return
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Starting scan...\n")
        
        try:
            result = subprocess.run(
                ["nuclei", "-u", target_url, "-t", template_path],
                capture_output=True, text=True
            )
            self.output_text.insert(tk.END, result.stdout)
            self.output_text.insert(tk.END, result.stderr)
        except Exception as e:
            self.output_text.insert(tk.END, f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NucleiGUI(root)
    root.mainloop()
