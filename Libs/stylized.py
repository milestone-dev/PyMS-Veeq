import Tkinter
import ttk
import json

# Set of wrappers that allows to easily configure Tkinter's widgets globally
# Made by Veeq7 for PyMS-Veeq
# After importing Tkinter with  `from Tkinter import *`
# Import using                  `from Libs.stylized import *`

dir_path = __file__.replace("/", "\\")
dir_path = dir_path[:dir_path.rfind("\\")]
dir_path = dir_path[:dir_path.rfind("\\")]
theme_file = dir_path + "\\Settings\\theme.txt"
default_theme = {
    "defaultBackground": "#222428",
    "defaultForeground": "#ffffff",
    "highlightForeground": "#ffffff",
    "highlightBackground": "#323438",
    "disabledForeground": "#181a1e",
    "disabledBackground": "#181a1e",
    "activeForeground": "#ffffff",
    "activeBackground": "#44464a",
    "selectedTextBackground": "#2244ff"
}

theme = {}

def init_ttk():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Horizontal.TScrollbar", bg=defaultBackground, troughcolor=defaultBackground)
    style.configure("Vertical.TScrollbar", bg=defaultBackground, troughcolor=defaultBackground)

def __load_theme():
    global theme
    try:
        with file(theme_file, 'r') as f:
            theme = json.load(f)
    except:
        theme = default_theme
        __save_default_theme()

def __save_default_theme():
    with file(theme_file, 'w') as f:
        json.dump(default_theme, f, sort_keys=True, indent=4)

def __get_color(name):
    if theme.has_key(name):
        return theme[name]
    return default_theme[name]

__load_theme()
defaultBackground = __get_color("defaultBackground")
defaultForeground = __get_color("defaultForeground")
highlightForeground = __get_color("highlightForeground")
highlightBackground = __get_color("highlightBackground")
disabledForeground = __get_color("disabledForeground")
disabledBackground = __get_color("disabledBackground")
activeForeground = __get_color("activeForeground")
activeBackground = __get_color("activeBackground")
selectedTextBackground = __get_color("selectedTextBackground")

def _configure(widget, hasText=False, hasHighlight=False, hasImage=False):
    widget.config(bg=defaultBackground)
    if hasText:
        widget.config(fg=defaultForeground)
    if hasHighlight:
        widget.config(highlightthickness=0, highlightcolor=highlightForeground, highlightbackground=highlightBackground)

    wClass = widget.__class__
    if issubclass(wClass, Button) or issubclass(wClass, Checkbutton) or issubclass(wClass, Radiobutton):
        widget.config(activebackground=activeBackground, activeforeground=activeForeground, disabledforeground=disabledForeground,
                      padx=3, pady=2)
        if issubclass(wClass, Checkbutton) or issubclass(wClass, Radiobutton):
            widget.config(selectcolor=activeBackground)
        elif hasImage:
            widget.config(relief = Tkinter.FLAT, borderwidth = 0)
    elif issubclass(wClass, Listbox):
        widget.config(selectbackground=selectedTextBackground)
        widget.config(borderwidth=1)
    elif issubclass(wClass, Entry):
        widget.config(selectbackground=selectedTextBackground)
        widget.config(disabledbackground=disabledBackground)
    elif issubclass(wClass, Frame):
        widget.config(borderwidth=0)


class Tk(Tkinter.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        Tkinter.Tk.__init__(self, screenName, baseName, className, useTk, sync, use)
        _configure(self, hasHighlight=True)


class Toplevel(Tkinter.Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Toplevel.__init__(self, master, cnf, **kw)
        _configure(self, hasHighlight=True)


class Frame(Tkinter.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Frame.__init__(self, master, cnf, **kw)
        _configure(self, hasHighlight=True)


class Button(Tkinter.Button):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Button.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True, hasImage=kw.has_key("image"))


class Checkbutton(Tkinter.Checkbutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Checkbutton.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class Radiobutton(Tkinter.Radiobutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Radiobutton.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class Label(Tkinter.Label):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Label.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class Text(Tkinter.Text):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Text.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True)


class Entry(Tkinter.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Entry.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class Canvas(Tkinter.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Canvas.__init__(self, master, cnf, **kw)
        _configure(self, hasHighlight=True)


class Listbox(Tkinter.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Listbox.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class Menu(Tkinter.Menu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Menu.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True)


class OptionMenu(Tkinter.OptionMenu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.OptionMenu.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class Scrollbar(ttk.Scrollbar):
    def __init__(self, master=None, cnf={}, **kw):
        ttk.Scrollbar.__init__(self, master, **kw)


# # Non-ttk version, changing color of this is impossible
# class Scrollbar(Tkinter.Scrollbar):
#     def __init__(self, master=None, cnf={}, **kw):
#         Tkinter.Scrollbar.__init__(self, master, cnf, **kw)
#         _configure(self, hasHighlight=True)


class LabelFrame(Tkinter.LabelFrame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.LabelFrame.__init__(self, master, cnf, **kw)
        _configure(self, hasText=True, hasHighlight=True)


class PanedWindow(Tkinter.PanedWindow):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.PanedWindow.__init__(self, master, cnf, **kw)
        _configure(self)