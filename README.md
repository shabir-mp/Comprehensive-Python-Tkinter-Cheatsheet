# Comprehensive Tkinter Cheatsheet 📃🏷
![Header](https://github.com/shabir-mp/Comprehensive-Tkinter-Cheatsheet/assets/133546000/74af8f4f-7cca-4cc3-a2af-4fc74cff4b03)
source : real python

## Introduction to Tkinter
Tkinter is a built-in Python module used to create graphical user interfaces (GUIs). It serves as a wrapper between Python and the Tk GUI toolkit created by Tcl/Tk. Tkinter provides various GUI widgets such as buttons, labels, text boxes, check boxes, and more, allowing users to create applications with interactive interfaces.

One of the advantages of Tkinter is that it comes as a standard module in the Python distribution, so there's no need to install additional packages to use it. Additionally, Tkinter is relatively easy to learn for beginners, as it has good documentation and many tutorials available.

The process of creating an interface using Tkinter involves creating widget objects and configuring their properties, such as size, position, and layout. After that, users can add business logic to the application, such as responding to user interactions with widgets or manipulating data.

Overall, Tkinter is a great choice for creating applications with graphical interfaces in Python, especially for small to medium-sized projects. However, for larger and more complex projects, some developers may opt for other GUI toolkits that are more powerful and flexible.

## History of Tkinter
Tkinter has a rich history within the Python programming language. Here's a brief overview:

1. **Early Development (Late 1980s - Early 1990s):** Tkinter's story begins with the creation of the Tcl (Tool Command Language) scripting language by John Ousterhout in the late 1980s. Tcl came with a graphical toolkit called Tk (Toolkit), which was developed by Ousterhout and his team at the University of California, Berkeley. Tk provided a set of graphical user interface widgets that could be used to build GUI applications.

2. **Integration with Python (Early 1990s):** In the early 1990s, Guido van Rossum, the creator of Python, recognized the potential of Tk for Python's graphical capabilities. He collaborated with others to integrate Tk into Python, creating Tkinter as the standard GUI toolkit for Python. Tkinter combined the simplicity and elegance of Python with the power and flexibility of Tk.

3. **Maturation and Standardization (1990s - 2000s):** Tkinter became an essential part of Python's standard library, ensuring its availability and consistency across different Python installations. Over the years, Tkinter continued to evolve, with improvements in performance, features, and compatibility.

4. **Continued Development (2010s - Present):** Tkinter remained a popular choice for Python developers due to its simplicity, ease of use, and cross-platform compatibility. Despite the emergence of alternative GUI toolkits and frameworks, Tkinter maintained its relevance and continued to be widely used in both small-scale and large-scale Python projects.

5. **Modernization Efforts (2010s - Present):** In recent years, efforts have been made to modernize Tkinter and enhance its capabilities. This includes updates to support newer versions of Python, improvements in documentation and tutorials, and community-driven initiatives to address usability issues and add new features.

Overall, Tkinter has a long and storied history as Python's standard GUI toolkit, playing a crucial role in enabling developers to create graphical applications with Python. Its simplicity, reliability, and integration with Python have made it a popular choice for developers of all levels of experience.

-------------------------------------
## 1. Importing Tkinter
```python
import tkinter as tk
```
Tkinter is usually imported using the `import tkinter as tk` statement. This allows us to access Tkinter classes and functions using the `tk` namespace.

## 2. Creating the Main Window
```python
root = tk.Tk()
```
The `Tk()` function creates the main window of the application, commonly referred to as the root window.

## 3. Creating a Label
```python
label = tk.Label(root, text="Hello, World!")
label.pack()
```
The `Label()` function creates a text label widget. It can display text or images. The `pack()` method is used to place the widget within the window.

## 4. Creating a Button
```python
button = tk.Button(root, text="Click Me!", command=callback_function)
button.pack()
```
The `Button()` function creates a clickable button widget. The `command` parameter specifies the function to be called when the button is clicked.

## 5. Creating an Entry (Input)
```python
entry = tk.Entry(root)
entry.pack()
```
The `Entry()` function creates a single-line text entry widget where users can input text. It allows users to enter text interactively.

## 6. Creating a Frame
```python
frame = tk.Frame(root)
frame.pack()
```
The `Frame()` function creates a container widget used to organize other widgets. It's useful for grouping related widgets together.

## 7. Layout Management
Tkinter provides two main layout managers: grid and pack.
### a. Grid Layout
```python
widget.grid(row=row_number, column=column_number)
```
The `grid()` method arranges widgets in rows and columns. Widgets are placed in specific rows and columns within the grid.
### b. Pack Layout
```python
widget.pack(side="top" / "bottom" / "left" / "right")
```
The `pack()` method organizes widgets in a block fashion. Widgets are packed against one edge of the container widget.

## 8. Handling Events
```python
def callback_function():
    # Do something when the event occurs
    pass

button = tk.Button(root, text="Click Me!", command=callback_function)
```
Event handling in Tkinter involves defining functions to execute when certain events occur, such as button clicks or key presses. These functions are then associated with specific widgets.

## 9. Displaying Images
```python
photo = tk.PhotoImage(file="image.png")
label = tk.Label(root, image=photo)
label.pack()
```
Tkinter supports displaying images using the `PhotoImage()` class. Images can be displayed within labels or other widgets.

## 10. Dialog Boxes
Tkinter provides various dialog boxes for user interaction.
### a. Message Box
```python
import tkinter.messagebox as mbox
mbox.showinfo("Title", "Message")
```
The `showinfo()` function displays an informational message box with a title and message.
### b. Input Dialog Box
```python
result = mbox.askquestion("Title", "Question?")
if result == "yes":
    # Do something if the user answers "yes"
```
The `askquestion()` function displays a dialog box with a question and returns the user's response.

## 11. Menu Bar
```python
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

menubar.add_cascade(label="File", menu=file_menu)
```
Tkinter supports creating menu bars with cascading menus. Menu items can be added with commands associated with them.

## 12. Running the Application
```python
root.mainloop()
```
The `mainloop()` function starts the Tkinter event loop, allowing the application to handle user inputs and events.

## Example of a Simple Tkinter Program
```python
import tkinter as tk

def greeting():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=greeting)
button.pack()

root.mainloop()
```
This is a basic example of a Tkinter program. It creates a window with a label, an entry field, and a button. When the button is clicked, it updates the label with a greeting message.

-----------------------------------------------------------------------------------------
![Github Footer](https://github.com/shabir-mp/Kereta-Api-Indonesia-Booking-System/assets/133546000/c1833fe4-f470-494f-99e7-d583421625be)
