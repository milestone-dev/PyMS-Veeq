
from Tkinter import *
from Libs.stylized import *


class AutohideScrollbar(Scrollbar):
	class Scrollbar(ttk.Scrollbar):
		def __init__(self, master=None, cnf={}, **kw):
			Scrollbar.__init__(self, master, **kw)
			self._hide = None
			self._show = None
			self._kwargs = {}

		def place(self, **kwargs):
			self._hide = ttk.Scrollbar.place_forget
			self._show = ttk.Scrollbar.place
			self._kwargs = kwargs
			Scrollbar.place(self, **kwargs)

		def pack(self, **kwargs):
			self._hide = ttk.Scrollbar.pack_forget
			self._show = ttk.Scrollbar.pack
			self._kwargs = kwargs
			Scrollbar.pack(self, **kwargs)

		def pack_nohide(self, **kwargs):
			Scrollbar.pack(self, **kwargs)

		def grid(self, **kwargs):
			self._hide = ttk.Scrollbar.grid_remove
			self._show = ttk.Scrollbar.grid
			self._kwargs = kwargs
			Scrollbar.grid(self, **kwargs)

		def set(self, lo, hi):
			if float(lo) <= 0.0 and float(hi) >= 1.0:
				if self._hide:
					self._hide(self)
			elif self._show:
				self._show(self, **self._kwargs)
			ttk.Scrollbar.set(self, lo, hi)
