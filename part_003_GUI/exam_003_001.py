# GUI - Graphical User Interface
# visual programming - Creating applications able to utilize GUI features
# controls or widgets - The GUI elements designed to receive such gestures
# focused widget - One of the widgets living inside a particular window owns the focus; the focus may change its owner, which is usually done by pressing the Tab key.
# the window has a title bar
# Inside the title bar there is (or can be) a set of control buttons (closing button)
# Inside the title bar (as the name suggests) there is a window title.

# active widgets (they can receive a user's clicks)
# One of these non-clickables is an icon – a small picture that usually helps the user to quickly identify the issue
# Another non-clickable member of the window's team is a label – a piece of text inside a window which literally explains the window's purpose.

# EDP - event-driven programming - You have to inform the event controller what you want to perform when a particular event, by writing event handlers
# event > trigger > event handler > event loop > event...
# An event handler is a piece of code responsible for responding to all clicks addressed to our button

# widget toolkit / GUI toolkit / UX library - adapter, for apps able to work under different operating environments that always look the same
# One of these toolkits TkInter - package named tkinter
# The GUI application itself consists of four essential elements:
# - importing the needed tkinter components;
# - an application’s main window;
# - adding a set of necessary widgets to the window;
# - launching the event controller.

# import tkinter
# or - import tkinter as tk; to create tk alias
# or choose elements - from tkinter import Button

import tkinter

# dialog boxes, dialog box is an example of a modal window - a window which grabs the whole of the application's focus
# It means that all other application widgets become deaf as long as the modal window is present
# as messagebox is a module located inside the tkinter package, we need to use the from variant of the import
from tkinter import messagebox

# The handler used by the button has to be a parameterless function of any name.
# Invoking your own handler is strictly prohibited, as it can completely confuse the event controller
# a function designed to be invoked by someone/something else (not us!) is often called a callback
def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    # messagebox.showinfo("info", "some\ninfo") # if you want to just show info with ok button
    if replay == 'yes':
        skylight.destroy();

# The main application window (which is often the only window being used by the application) is created by the tkinter method named Tk().
skylight = tkinter.Tk()

# add title
skylight.title("Skylight")

# it can be said that the button creates itself, but to make it visible, you need the window's (not the button's!) method.
# Its first argument (which is a reference to the target window) is obligatory
# - the widget's coordinates refer defaultly to the pixel occupied by the upper-left corner;
# - the widget's size is defaultly determined by the constructor in order to fit the widget's content (the title's length and height in this case)
# - the widget's location is measured in pixels
# binding the callback with the widget by using the command constructor's parameter is not the only way offered by tkinter for this purpose;
# callbacks can be replaced during program execution – we'll tell you more about that soon;
# the one and same callback can be bound with more than one widget – it's a very useful solution in some cases.
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)

# The object returned by the method is complete, but at the same time, completely invisible. Moreover, it won't be visible until the event controller starts.
# To start the controller, you have to invoke the main window's method, named mainloop().
skylight.mainloop()

# ===================================================

# geometry managers (these managers cannot be mixed in one application):

# place - precisely declare a widget's location - pixel by pixel
# element.place(x=10, y=10, width=150, height=50)

# grid - It gives you a chance to express your general wishes and tries to deploy the widgets according to them
# window's interior is divided into a number of columns of equal width and a number of rows of equal height
# element.grid(row=2, column=0, columnspan=2, rowspan=2)

# pack - tkinter try to find the best location
# The default pack's operation tends to deploy all subsequent widgets in one column, one below the other
# element.pack(
#   side=tkinter.TOP | tkinter.BOTTOM | tkinter.LEFT | tkinter.RIGHT,
#   fill=tkinter.NONE | tkinter.X | tkinter.Y | tkinter.BOTH,
# )

# ====================================================
# Colors
# button = tk.Button(
#   window,
#   text="Title",
#   bg="red",
#   fg="yellow",
#   activeforeground="LavenderBlush",
#   activebackground="HotPink
#  )

# for colors you can use: 
# - English color's name, 
# - 750 predefined color names,
# - RGB color model ("#00FF00")

# ==================================================
# Label – a non-clickable widget able to present short textual information
# label = tk.Label(window, text = "Little label:")

# Frame - non-clickable component used to group widgets and to separate them (visually) from other window components
# frame = tk.Frame(window, height=30, width=100, bg="#000099")

# Button
# button = tkinter.Button(skylight, text="Bye!", command=Click)

# IntVar - This object is designed to store integer values. Objects of the IntVar class are used by tkinter to organize internal communication between different widgets. A regular variable can't play such a role.
# switch = tk.IntVar()
# switch.set(1)

# Checkbutton - It’s a small square which can be filled with a tick mark, or which can be empty. used to represent two-state selections
# check IntVar above
# switch == 1 > ON; switch == 0 > OFF
# you don't have to click on Checkbutton, it dynamicly reflects switch value
# checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)

# Entry - (input field) designed to let the user enter simple, one-line data, like single numbers, names, addresses, etc. 
# entry = tk.Entry(window, width=30)

# Radiobutton - small circles filled with a dot, or not
# Checkbuttons are solitary (they work individually) while Radiobuttons always work in groups and – note it! – only one of the widgets inside the group can be checked. Clicking an unchecked member of the group will cause the currently checked Radiobutton to change its state.
# variable - binds a switch object to both of the widgets, and this is the clue – the fact that both Radiobuttons are bound to the same object creates the group. Don’t forget that!
# Value - distinguishes the Radiobuttons inside the group, and thus each of the Radiobuttons has to use a different value (we’ve used 0 and 1)
# radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
# radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)

#  ==========================================================

# Events
# widget.bind(event, callback)
# widget.unbind(event)
# binds/unbind a callback to all currently existing widgets
# window.bind_all(event, callback)
# window.unbind_all(event)
# Q: What is an event from the event controller’s point of view?
# A: It’s an object carrying some useful info about what actually happens when the event has been induced (by the user or by another factor).
# Q: How are the events identified?
# A: By unique names – each event has its own name and the name is just a unified string.

# callback for comand = parameterless
# callback for bind = 1 parameter
# you can manage it like below
# def callback(ev=None):

# An event object is an instantiation of the Event class

# unbind widget (wid) prop:
# wid.config(prop=val)
# b1.config(command=lambda:None)

# =========================================================
#  widget's properties

# You have to use one of two possible ways of reading and setting widget properties’ values
# button = tk.Button(window, text="OFF", command=on_off)
# 1.
# old_text = button["text"]
# button["text"] = "new text"
# 
# 2.
# old_val = button.cget("text")
# button.config(text="new_val")

# Font - in tkinter as tuples
# ("font_family_name", "font_size")
# ("font_family_name", "font_size", "font_style")
# font_style:
# - "bold"
# - "italic"
# - "underline"
# - "overstrike"
# label_2 = tk.Label(window, text="Text", font=("Times", "12", "bold"))

# Sizes:
# - borderwidth: The width of the 3D-frame surrounding some widgets (e.g., Button)
# - highlightthickness: The width of the additional frame drawn around the widget when it gains the focus
# - pady/padx: The width/height of an additional empty space/margin around the widget
# - wraplength: If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
# - height: The height of the widget
# - underline: The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback to work – no automation here, sorry)
# - width: The width of the widget
# 
# button_2 = tk.Button(window, text="Exceptional button")
# button_2.pack()
# button_2["borderwidth"] = 10
# button_2["highlightthickness"] = 10
# button_2["padx"] = 10
# button_2["pady"] = 5
# button_2["underline"] = 1

# Colors:
# - bg:	The color of the widget’s background (you can freely use either of these two forms)
# - fg: The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)
# - activebackground/activeforeground: Like bg and fg but used when the widget becomes active
# - disabledforeground: The width of the widget

# anchor - point inside the widget to which the text (if any) is anchored:
# CENTER (default) + compass coordinates
# button_2 = tk.Button(window, text="Another button")
# button_2["anchor"] = SW

# cursor:
# label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
# arrow (default), clock, heart, etc...

# =================================================================
# Widget methods
# 
# widget.after(milisaconds, callback) - do callback only once after time
# widget.after_cancel(id)
# widget.destroy() - It removes the widget's objeck and recursive thier ansestors completely
# widget.focus_get() - returns a reference to the currently focused widget or None - callable on any widget
# widget.focus_set() - focuses the widget

#  ===============================================================
# Observable variable:
# - object of the container class
# - has to be explicitly created and initialized
# - these variables are typed
# - can only be created after the main window initialization

# Types: 
# - BooleanVar - 0
# - DoubleVar - 0.0
# - IntVar - False
# - StringVar - ""

# variable.set("value") - to set value of variable
# variable.get() - to get value from variable

# Each observable variable can be enriched with a number of observers
# An observer is a function (a kind of callback) which will be invoked automatically each time a specified event occurs in the variable’s life.
# Adding an observer to a variable is done by a method named trace():
# obsid = variable.trace(trace_mode, observer)
# variable.trace_vdelete(trace_mode,obsid) - remove the observer
# trace_mode: 
# "r" – if you want to be aware of the variable reads (accessing its value through get())
# "w" – if you want to be aware of the variable writes (changing its value through set())
# "u" – if you want to be aware of the variable’s annihilation (removing the object through del)
# obsid – the observer’s identifier obtained from the previous trace() invocation

# def observer(id, ix, act):
# 
# id – an internal observable variable identifier (unusable for us);
# ix – an empty string (always – don’t ask us why, it’s tkinter’s business)
# act – a string informing us what happened to the variable or, in other words, what reason triggered the observer ('r', 'w' or 'u')
