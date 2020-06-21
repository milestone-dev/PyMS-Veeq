import Tkinter

# Set of wrappers that allows to easily configure Tkinter's widgets globally
# Made by Veeq7 for PyMS-Veeq
# After importing Tkinter with  `from Tkinter import *`
# Import using                  `from Libs.stylized import *`

def configure(widget, hasText=False, hasHighlight=False):
    wClass = widget.__class__

    defaultBackground = "#222428"
    defaultForeground = "#ffffff"
    highlightForeground = "#ffffff"
    highlightBackground = "#323438"
    disabledBackground = "#66687c"
    activeBackground = "#44464a"
    selectedTextBackground = "#2244ff"

    widget.config(bg=defaultBackground)
    if hasText:
        widget.config(fg=defaultForeground)

    if hasHighlight:
        widget.config(highlightthickness=0, highlightcolor=highlightForeground, highlightbackground=highlightBackground)

    if wClass == Button or wClass == Checkbutton or wClass == Radiobutton:
        widget.config(activebackground=activeBackground, activeforeground=highlightBackground, disabledforeground=disabledBackground, padx=3, pady=2)

        if wClass == Checkbutton or wClass == Radiobutton:
            widget.config(selectcolor=activeBackground)

    if wClass == Entry:
        widget.config(selectbackground=selectedTextBackground)

    if wClass == Scrollbar:
        widget.config(troughcolor=defaultBackground)


class Tk(Tkinter.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        Tkinter.Tk.__init__(self, screenName, baseName, className, useTk, sync, use)
        configure(self, hasHighlight=True)


class Toplevel(Tkinter.Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Toplevel.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Frame(Tkinter.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Frame.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Button(Tkinter.Button):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Button.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Checkbutton(Tkinter.Checkbutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Checkbutton.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Radiobutton(Tkinter.Radiobutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Radiobutton.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Label(Tkinter.Label):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Label.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Text(Tkinter.Text):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Text.__init__(self, master, cnf, **kw)
        configure(self, hasText=True)


class Entry(Tkinter.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Entry.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Scale(Tkinter.Scale): # TODO: Check if it has Highlight
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Scale.__init__(self, master, cnf, **kw)
        configure(self)


class Canvas(Tkinter.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Canvas.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Listbox(Tkinter.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Listbox.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Menu(Tkinter.Menu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Menu.__init__(self, master, cnf, **kw)
        configure(self, hasText=True)


class OptionMenu(Tkinter.OptionMenu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.OptionMenu.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Listbox(Tkinter.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Listbox.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Scrollbar(Tkinter.Scrollbar):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Scrollbar.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class LabelFrame(Tkinter.LabelFrame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.LabelFrame.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)