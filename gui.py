import tkinter as tk
from tkinter import filedialog, simpledialog
from splitting.splitter import splitter

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_name = file_path#.split("/")[-1]  # Extract just the file name from the path
        range_list = simpledialog.askstring("Page Range", f"Enter Page Range (e.g., '1-5'):")
        pages = range_list.split(',')
        for page_range in pages:
            i = 0
            for char in page_range:
                i=i+1
                if char=='-':
                    break
            start = page_range[0:i-1]
            end = page_range[i:len(page_range)]
            tk.messagebox.showinfo("Selected PDF and Page Range",
                                   f"Selected PDF File: {file_name}\nPage Range: {page_range}")
            a=int(start)
            b=int(end)
            splitter(file_name, [a, b])
        tk.messagebox.showinfo("PDF Splitting done!","PDF has been splitted! Check the directory of the original PDF.")

# Create the main window
root = tk.Tk()
root.title("PDF File Selector")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open PDF File", command=open_pdf)
open_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
