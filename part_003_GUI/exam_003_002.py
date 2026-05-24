# widget = Widget(master_widget, option, ... )
# master widget - main window, Frame or LabelFrame

# all widgets fall into two categories: clickable and non-clickable

# Button:
# command - callback
# justify - text position: LEFT, CENTER, and RIGHT
# state - you can set to DISABLED or NORMAL, when the mouse is located above the button, the property changes its value to ACTIVE
# flash() - the button flashes a few times but doesn’t change its state
# invoke() - activates the callback - only way to invoke your own callback explicitly

# Checkbutton:
# bd - the checkbutton frame width (default is two pixels)
# command - callback
# justify - text position: LEFT, CENTER, and RIGHT
# state - you can set to DISABLED or NORMAL, when the mouse is located above the button, the property changes its value to ACTIVE
# variable - an observable IntVar variable, dy default checked=1 unchecked=0
# offvalue - unchecked value
# onvalue - checked value
# deselect() - unchecks the widget
# flash() - the button flashes a few times but doesn’t change its state
# invoke() - activates the callback - only way to invoke your own callback explicitly
# select() - checks the widget
# toggle() - toggles the widget (changes its state to the opposite one

# Radiobutton:
# command - callback
# justify - text position: LEFT, CENTER, and RIGHT
# state - you can set to DISABLED or NORMAL, when the mouse is located above the button, the property changes its value to ACTIVE
# variable 	an observable IntVar or StringVar variable reflecting the current selection within the Radiobutton’s group; changing the variable’s value automatically changes the selection
# value - a unique value within the group
# deselect() - unchecks the widget
# flash() - the button flashes a few times but doesn’t change its state
# invoke() - activates the callback - only way to invoke your own callback explicitly
# select() - checks the widget

# Label:
# text - string for text
# textvariable - variable fot text (dynamicly)

# Message - very similar to the Label but is able to format the presented text by fitting it automatically to the widget’s size:
# text - string for text
# textvariable - variable fot text (dynamicly)

# Frame - container; when you place a widget inside a Frame, you measure its location relative to the Frame’s upper-left corner:
# takefocus - 0 = no recived focus (default), 1 = recived focus

# LabelFrame - Frame enriched with a visible border and a title
# takefocus - 0 = no recived focus (default), 1 = recived focus
# text
# labelanchor - texxt placement, 12 compas directions eg. 'se', 'es', 'n'

# Entry:
# command 	although Entry is obviously a clickable widget, it doesn’t allow you to bind a callback through the command property. You can observe and control all occurring changes instead by setting the tracer function for the observable variable which cooperates with Entry (we’ll show you this – be patient!)
# show - what to show insted of charackters, eg. show='*' for password
# state - you can set to DISABLED or NORMAL, when the mouse is located above the button, the property changes its value to ACTIVE
# textvariable - an observable StringVar reflecting the current state of the input field
# width - the input field’s width (in characters)
# get() - returns the current input field’s contents as a string
# set(s) - sets the whole input field’s contents with the s string
# delete(first, last=None)  - deletes a part of the input field’s contents; first and last can be integers with values indexing the string; if the last argument is omitted, a single character is deleted; if last is specified as END, it points to the place after the last field’s character
# insert(index, s) - inserts the s string at the field position pointed to by index

# def callback(*args):
#   entry_value = text.get()
#   text.set(last_string) # you can modify entry_value
# text = tk.StringVar()
# entry = tk.Entry(window, textvariable=text)
# text.trace('w', callback)

#  =================================================================

# Menu:
# - a classic menu is actually a horizontal bar located at the top of the application window;
# - the bar contains a number of horizontally deployed options, often referred to as items or entries;
# - these options can have hot-keys (keyboard shortcuts enabling the user to quickly access selected operations without using a mouse; usually, hot-keys are triggered by pressing Alt-hotkey on the keyboard)
# - selecting a menu’s option (it doesn’t matter whether through a hotkey or by a mouse click) causes one of two effects:
#     it launches a callback bound to the option;
#     it unrolls a new menu (actually a submenu)
# - if you want to have such a menu within your Tkinter application, you have to:
#     create a top-level menu object;
#     embed it inside the window;
#     bind a number of required submenus (this is called a cascade) or connect a single callback.

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu) # tearoff=0 - remove dashes - some old legacy
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=3) # underline=3 - some hotkey for expand submenu
# sub_menu_file.add_command(label="Open...", command=callback)
# sub_menu_file.add_separator() # separator is here!
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure, accelerator="Ctrl-Q") # add item to submenu; underline=0 (sets Alt-F as a hotkey); accelerator - right text 
# main_menu.add_command(label="About...", command=about_app, underline=1) # underline=1 (sets Alt-B as a hotkey)
# window.bind_all("<Control-q>", callback) # set hot key - check accelerator above

# you cannot modify any of the (sub)menu item by using the standard config() method invocation, because from tkinter's point of view, the item is not a widget – it’s only a very specific widget component. 
# If you want to manipulate a menu’s item, you should use a dedicated method named entryconfigure(). The method accepts two parameters:
# item.entryconfigure(i, prop=value)
# the first is an integer index of the modified item (entry)
# the second is a keyworded argument pointing to the modified property
# sub_menu.entryconfigure(1, state=accessible)

# ======================================================================

# Main window

# window.title("Text") # change window title

# window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png')) # exchange the window’s icon with the one provided
# - prepare an icon as a PNG image;
# - put the image in the same directory where the application resides;
# - use a PhotoImage class constructor to convert the PNG file into an internal tkinter representation (PhotoImage() is a part of tkinter, and we’re going to tell you more about it soon

# window.geometry("100x100") # size of window - "width x heigth"

# window.minsize(width=250, height=200) # window min size
# window.maxsize(width=500, height=300) # window max size
# window.resizable(width=False, height=False) # is window resizable in dimention

# window.protocol("WM_DELETE_WINDOW", really) # callback on main window close btn

# ============================================================

# Messagebox
# All these functions display a modal dialog window and wait for a user response. The dialog’s behavior is determined by three parameters:

# title – a string displayed in the dialog’s title bar (it can’t be very long, of course);
# message – a string displayed inside the dialog; note: the \n plays its normal role and breaks up the message’s lines;
# options – a set of options shaping the dialog in a non-default way, two of which are useful to us:
#     default – sets the default (pre-focused) answer; usually, it’s focused on the button located first from the left; this can be changed by setting the keyword argument with identifiers like CANCEL, IGNORE, OK, NO, RETRY, and YES;
#     icon – sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION, and WARNING.

# answer = messagebox.askyesno("?", "To be or not to be?") # returns True or False; dialog containing a question mark
# answer = messagebox.askokcancel("?", "I'm going to format your hard drive") # returns True or False; dialog containing a question mark
# answer = messagebox.askretrycancel("?", "I'm going to format your hard drive") # returns True or False; dialog containing a warning sign
# answer = messagebox.askquestion("?", "I'm going to format your hard drive") # returns "Yes" or "No"
# answer = messagebox.showerror("!", "Your code does nothing!") # returns OK; It displays a red warning
# answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!") # returns OK; It displays a red warning

# =============================================================

# Canvas

# options:
# - borderwidth - canvas border’s width in pixels (default: 2)
# - background (bg) - canvas border’s color (default: the same as the underlying window’s color)
# - height - canvas height (in pixels)
# - width - canvas width (in pixels)

# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380) # draw triancle

# canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option...) # polygonal chain
# arrow - normally, the chain ends aren’t marked in any special way, but you may want them to be finished with arrowheads;
#           setting the arrow option to FIRST results in drawing an arrowhead at the chain’s beginning,
#           LAST at the chain’s end,
#           BOTH at both sides of the chain.
# fill - chain color (setting the option to an empty string causes the line to be transparent)
# smooth - setting it to True rounds the chain’s corners using a set of connected parabolas
# width - line width (default: 1 pixel)

# canvas.create_rectangle(x0, y0, x1, y1, option...) # rectancle
# - outline - rectangle edge color (if specified as an empty string, the edge is transparent)
# - fill - rectangle interior color
# - width - rectangle edge width in pixels (default: 1)

# canvas.create_polygon(x0, y0, x1, y1, xn, yn, option...) # polygon - last segment (connecting the first and the last points) in the chain is drawn automatically
# - create_polygon props

# c.create_oval(middle_x, middle_y, width_x, width_y, option...) # ellipse
# - create_polygon props

# canvas.create_arc(x0,y0,x1,y1,option...) # The method draws the arc of an ellipse inscribed inside a rectangle with vertices at points (x0,y0) and (x1,y1).
# - create_polygon props +
# - style - can be set to one of the following:
#           PIESLICE (default),
#           CHORD,
#           ARC,
# - start - the angle (in degrees) of the arc’s start relative to the X-axis (e.g., 90 means the highest point of the ellipse, while 0 is the right-most point. The default is 0)
# - extent - the arc’s span (in degrees) relative to the start point; note: the span is calculated counter-clockwise. The default is 90 (a quarter of an ellipse)

# c.create_text(x, y, option...) # text
# - fill - text color
# - font - text font
# - justify - text justification: LEFT (default), CENTER, RIGHT
# - text - text to display (\n works as expected)
# - width - normally, the rectangle is as wide as the longest text line; using the width option forces the text to be aligned to that size\

# canvas.create_image(x, y, option...) # image
# - image - an object of the PhotoImage class containing the image itself;
#           the PhotoImage class constructor needs a keyword argument named file pointing to a bitmap file (note: only GIF and PNG formats are accepted);
#           the argument should specify the file’s path
# image = tk.PhotoImage(file='logo.png')
# canvas.create_image(200, 200, image=image)

# JPEG image:
# import PIL # import the Image and ImageTk classes from the PIL (Python Image Library) module;
# jpg = PIL.Image.open('logo.jpg') # build an object of the Image() class and use its open() method to fetch the bitmap from the file (the argument should specify the file’s path)
# image = PIL.ImageTk.PhotoImage(jpg) # convert this object into a PhotoImage class object using an ImageTk function of the same name;
# canvas.create_image(200, 200, image=image)
