import Tkinter, ttk
import tkMessageBox
import os.path, json

# Set of wrappers that allows to easily configure Tkinter's widgets globally
# Made by Veeq7 for PyMS-Veeq
# After importing Tkinter with  `from Tkinter import *`
# Import using                  `from Libs.stylized import *`


def __get_theme_file_path():
    __dir_path = __file__.replace("/", "\\")
    __dir_path = __dir_path[:__dir_path.rfind("\\")]
    __dir_path = __dir_path[:__dir_path.rfind("\\")]
    return __dir_path + "\\Settings\\theme.txt"


__theme_file_path = __get_theme_file_path()
__default_theme = {
    "defaultBackground": "#222428",
    "defaultForeground": "#cccccc",
    "activeForeground": "#cccccc",
    "activeBackground": "#44464a",
    "disabledForeground": "#686a6e",
    "disabledBackground": "#282a2e",
    "selectedBackground": "#2244ff",
    "isCustomized": False
}

__theme = {}


def __theme_file_exists():
    return os.path.isfile(__theme_file_path)


def __load_theme():
    global __theme
    try: # Load theme from file
        with file(__theme_file_path, 'r') as f:
            __theme = json.load(f)
    except ValueError, e: # If there is a JSON error then inform the user
        if __theme_file_exists():
            tkMessageBox.askquestion("Theme File Exception", "Your theme definition file is invalid. Error Message:\n\"" + e.message + "\"", type="ok", icon="error")
            exit(-1)
    except IOError, e: # If there is no file, then save default theme
        if not __theme_file_exists():
            __save_default_theme()

    # If loaded successfully then..
    if __theme_file_exists() and __theme != __default_theme: # If theme is different than default and was not customized then overwrite the theme with default one
        if __theme.has_key("isCustomized"):
            if not __theme.get("isCustomized"):
                __save_default_theme()
        else:
            __save_default_theme()


def __save_default_theme(): # Save and enable default theme
    global __theme
    __theme = __default_theme
    with file(__theme_file_path, 'w') as f:
        json.dump(__default_theme, f, indent=4, sort_keys=True)


__load_theme()
__defaultBackground = __theme.get("defaultBackground")
__defaultForeground = __theme.get("defaultForeground")
__disabledForeground = __theme.get("disabledForeground")
__disabledBackground = __theme.get("disabledBackground")
__activeForeground = __theme.get("activeForeground")
__activeBackground = __theme.get("activeBackground")
__selectedTextBackground = __theme.get("selectedTextBackground")


def init_ttk():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Horizontal.TScrollbar", bg=__defaultBackground, troughcolor=__defaultBackground)
    style.configure("Vertical.TScrollbar", bg=__defaultBackground, troughcolor=__defaultBackground)


def _configure(widget, hasText=False, hasHighlight=False, hasImage=False):
    widget.config(bg=__defaultBackground)
    if hasText:
        widget.config(fg=__defaultForeground)
    if hasHighlight:
        widget.config(highlightthickness=0)

    wClass = widget.__class__
    if issubclass(wClass, Button) or issubclass(wClass, Checkbutton) or issubclass(wClass, Radiobutton):
        widget.config(activebackground=__activeBackground, padx=3, pady=2)
        if issubclass(wClass, Checkbutton) or issubclass(wClass, Radiobutton):
            widget.config(selectcolor=__activeBackground)
        elif hasImage:
            widget.config(relief = Tkinter.FLAT, borderwidth = 0)
    elif issubclass(wClass, Listbox):
        widget.config(selectbackground=__selectedTextBackground)
        widget.config(borderwidth=1)
    elif issubclass(wClass, Entry):
        widget.config(selectbackground=__selectedTextBackground)
        widget.config(disabledbackground=__disabledBackground)
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