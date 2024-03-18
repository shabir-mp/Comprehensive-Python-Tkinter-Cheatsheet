import tkinter as tk
from tkinter import messagebox

# Function to display text on label
def display_text():
    text = input_text.get()
    if text:
        label_text.config(text="You entered: " + text)
    else:
        messagebox.showerror("Error", "Please enter some text.")

# Function to clear the input field
def clear_input():
    input_text.delete(0, tk.END)
    label_text.config(text="")

# Initialize the root window
root = tk.Tk()
root.title("Tkinter Example Application")

# Create a label for input instruction
label_input = tk.Label(root, text="Enter text:")
label_input.pack()

# Create an entry for text input
input_text = tk.Entry(root)
input_text.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create a button to display text
button_display = tk.Button(button_frame, text="Display", command=display_text)
button_display.pack(side=tk.LEFT, padx=5)

# Create a button to clear input
button_clear = tk.Button(button_frame, text="Clear", command=clear_input)
button_clear.pack(side=tk.LEFT, padx=5)

# Create a label to display the input text
label_text = tk.Label(root, text="")
label_text.pack()

# Run the main loop
root.mainloop()
