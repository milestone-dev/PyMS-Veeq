import Tkinter

# Set of wrappers that allows to easily configure Tkinter's widgets globally
# Made by Veeq7 for PyMS-Veeq
# After importing Tkinter with  `from Tkinter import *`
# Import using                  `from Libs.stylized import *`

def configure(widget, hasText=False, hasHighlight=False, isButton=False, isScrollbar=False):
    widget.config(bg="#222222", borderwidth=1)

    if hasText:
        widget.config(fg="#ffffff")

    if hasHighlight:
        widget.config(highlightthickness=0, highlightcolor="#333333", highlightbackground="#333333")

    if isButton:
        widget.config(fg="#ffffff")
        #widget.config(activebackground="#444444", activeforeground="#fffffff")
        pass

    if isScrollbar:
        widget.config(troughcolor="#333333")


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
        configure(self, hasText=True, hasHighlight=True, isButton=True)


class Checkbutton(Tkinter.Checkbutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Checkbutton.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True, isButton=True)


class Radiobutton(Tkinter.Radiobutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Radiobutton.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True, isButton=True)


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


class Scale(Tkinter.Scale):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Scale.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Canvas(Tkinter.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Canvas.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Listbox(Tkinter.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Listbox.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Menu(Tkinter.Menu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Menu.__init__(self, master, cnf, **kw)
        configure(self)


class OptionMenu(Tkinter.OptionMenu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.OptionMenu.__init__(self, master, cnf, **kw)
        configure(self, hasHighlight=True)


class Listbox(Tkinter.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Listbox.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)


class Scrollbar(Tkinter.Scrollbar):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Scrollbar.__init__(self, master, cnf, **kw)
        configure(self, isScrollbar=True, hasHighlight=True)


class LabelFrame(Tkinter.LabelFrame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.LabelFrame.__init__(self, master, cnf, **kw)
        configure(self, hasText=True, hasHighlight=True)