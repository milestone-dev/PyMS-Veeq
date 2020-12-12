import Tkinter, ttk
import tkMessageBox
import os.path, json

# Set of wrappers that allows to easily configure Tkinter's widgets globally
# Made by Veeq7 for PyMS-Veeq
# After importing Tkinter with  `from Tkinter import *`
# Import using                  `from Libs.stylized import *`

def __get_theme_dir_path():
    __dir_path = __file__.replace("/", "\\")
    __dir_path = __dir_path[:__dir_path.rfind("\\")]
    return __dir_path[:__dir_path.rfind("\\")] + "\\Settings"


__theme_dir_path = __get_theme_dir_path()
__theme_file_path = __theme_dir_path + "\\theme.txt"
__default_theme = {
    "defaultBackground": "#181a1e",
    "defaultForeground": "#cccccc",
    "activeBackground": "#44464a",
    "activeForeground": "#cccccc",
    "enabledBackground": "#222428",
    "enabledForeground": "#cccccc",
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
    if not os.path.exists(__theme_dir_path):
        os.mkdir(__theme_dir_path)
    with file(__theme_file_path, 'w') as f:
        json.dump(__default_theme, f, indent=4, sort_keys=True)


__load_theme()
stylized_theme_default_background = __theme.get("defaultBackground")
stylized_theme_default_foreground = __theme.get("defaultForeground")
stylized_theme_disabled_background = __theme.get("disabledBackground")
stylized_theme_disabled_foreground = __theme.get("disabledForeground")
stylized_theme_enabled_background = __theme.get("enabledBackground")
stylized_theme_enabled_foreground = __theme.get("enabledForeground")
stylized_theme_active_foreground = __theme.get("activeForeground")
stylized_theme_active_background = __theme.get("activeBackground")
stylized_theme_selected_text_background = __theme.get("selectedTextBackground")


def stylized_ttk_init():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Horizontal.TScrollbar", bg=stylized_theme_default_background, troughcolor=stylized_theme_default_background)
    style.configure("Vertical.TScrollbar", bg=stylized_theme_default_background, troughcolor=stylized_theme_default_background)


def stylized_widget_configure(widget, is_button_with_image=False):
    config = widget.config()

    widgetConfig = {}

    if config.has_key("bg"):
        widgetConfig.update({"bg":stylized_theme_default_background})
    if config.has_key("fg"):
        widgetConfig.update({"fg":stylized_theme_default_foreground})
    if config.has_key("activebackground"):
        widgetConfig.update({"activebackground":stylized_theme_active_background})
    if config.has_key("activeforeground"):
        widgetConfig.update({"activeforeground":stylized_theme_active_foreground})
    if config.has_key("disabledbackground"):
        widgetConfig.update({"disabledbackground":stylized_theme_disabled_background})
    if config.has_key("disabledforeground"):
        widgetConfig.update({"disabledforeground":stylized_theme_disabled_foreground})
    if config.has_key("selectbackground"):
        widgetConfig.update({"selectbackground":stylized_theme_selected_text_background})

    if config.has_key("highlightthickness"):
        widgetConfig.update({"highlightthickness":0})
    if config.has_key("borderwidth"):
        if widget.cget("borderwidth") > 0:
            widgetConfig.update({"borderwidth":1})

    if config.has_key("relief"):
        if "" != widget.cget("relief") != Tkinter.FLAT != "":
            widgetConfig.update({"relief":Tkinter.GROOVE})
    if config.has_key("offrelief"):
        if "" != widget.cget("offrelief") != Tkinter.FLAT != "":
            widgetConfig.update({"offrelief":Tkinter.GROOVE})
    if config.has_key("overrelief"):
        if "" != widget.cget("overrelief") != Tkinter.FLAT:
            widgetConfig.update({"overrelief":Tkinter.GROOVE})

    if config.has_key("padx"):
        widgetConfig.update({"padx":3, "pady":2})

    wClass = widget.__class__
    if issubclass(wClass, Button) or issubclass(wClass, Checkbutton) or issubclass(wClass, Radiobutton):
        if issubclass(wClass, Checkbutton) or issubclass(wClass, Radiobutton):
            widgetConfig.update({"selectcolor":stylized_theme_active_background})
            if widget.cget("indicatoron") == 0:
                widgetConfig.update({"foreground":stylized_theme_enabled_foreground, "background":stylized_theme_enabled_background})
        elif issubclass(wClass, Button):
            if is_button_with_image:
                widgetConfig.update({"overrelief":Tkinter.SUNKEN, "background":stylized_theme_enabled_background})
            elif widget.cget("relief") != Tkinter.FLAT and widget.cget("borderwidth") > 0:
                widgetConfig.update({"foreground":stylized_theme_enabled_foreground, "background":stylized_theme_enabled_background})
    elif issubclass(wClass, Entry) or issubclass(wClass, Listbox) or issubclass(wClass, Text):
        widgetConfig.update({"foreground":stylized_theme_enabled_foreground, "background":stylized_theme_enabled_background})

    widget.config(widgetConfig)

class Tk(Tkinter.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        Tkinter.Tk.__init__(self, screenName, baseName, className, useTk, sync, use)
        stylized_widget_configure(self)


class Toplevel(Tkinter.Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Toplevel.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Frame(Tkinter.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Frame.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Button(Tkinter.Button):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Button.__init__(self, master, cnf)
        stylized_widget_configure(self, is_button_with_image=kw.has_key("image"))
        self.config(**kw)


class Checkbutton(Tkinter.Checkbutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Checkbutton.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Radiobutton(Tkinter.Radiobutton):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Radiobutton.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Label(Tkinter.Label):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Label.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Text(Tkinter.Text):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Text.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Entry(Tkinter.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Entry.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Canvas(Tkinter.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Canvas.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Listbox(Tkinter.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Listbox.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Menu(Tkinter.Menu):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.Menu.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class Scrollbar(ttk.Scrollbar):
    def __init__(self, master=None, cnf={}, **kw):
        ttk.Scrollbar.__init__(self, master, **kw)


# # Non-ttk version, changing color of this is impossible
# class Scrollbar(Tkinter.Scrollbar):
#     def __init__(self, master=None, cnf={}, **kw):
#         Tkinter.Scrollbar.__init__(self, master, cnf)
#         _configure(self)
#         self.config(**kw)


class LabelFrame(Tkinter.LabelFrame):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.LabelFrame.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)


class PanedWindow(Tkinter.PanedWindow):
    def __init__(self, master=None, cnf={}, **kw):
        Tkinter.PanedWindow.__init__(self, master, cnf)
        stylized_widget_configure(self)
        self.config(**kw)