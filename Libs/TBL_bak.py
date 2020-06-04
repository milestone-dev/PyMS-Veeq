from utils import *
from fileutils import *

import struct, re

TBL_REF = """#----------------------------------------------------
# Misc.
#    <0> = End Substring
#    <9> = Tab
#   <10> = Newline
#   <18> = Right Align
#   <19> = Center Align
#   <27> = Escape Key
#   <35> = #
#   <60> = <
#   <62> = >
#
# Menu Screen Colors
#    <1> = Cyan
#    <2> = Cyan
#    <3> = Green
#    <4> = Light Green
#    <5> = Grey*
#    <6> = White
#    <7> = Red
#    <8> = Black*
#   <11> = Invisible*
#   <12> = Truncate
#   <14> = Black
#   <15> = Black
#   <16> = Black
#   <17> = Black
#   <20> = Invisible*
#   <21> = Black
#   <22> = Black
#   <23> = Black
#   <24> = Black
#   <25> = Black
#   <26> = Black/Cyan?
#   <27> = Black
#   <28> = Black
#
# In-game Colors
#    <1> = Cyan
#    <2> = Cyan
#    <3> = Yellow
#    <4> = White
#    <5> = Grey*
#    <6> = Red
#    <7> = Green
#    <8> = Red (Player 1)
#   <11> = Invisible*
#   <12> = Truncate
#   <14> = Blue (Player 2)
#   <15> = Teal (Player 3)
#   <16> = Purple (Player 4)
#   <17> = Orange (Player 5)
#   <20> = Invisible*
#   <21> = Brown (Player 6)
#   <22> = White (Player 7)
#   <23> = Yellow (Player 8)
#   <24> = Green (Player 9)
#   <25> = Brighter Yellow (Player 10)
#   <26> = Cyan (Player 12)
#   <27> = Pinkish (Player 11)
#   <28> = Dark Cyan
#   <29> = Greygreen
#   <30> = Bluegrey
#   <31> = Turquiose
#
# Hotkey Types
#    <0> = Label Only, no Requirements
#    <1> = Minerals, Gas, Supply (Unit/Building)
#    <2> = Upgrade Research
#    <3> = Spell
#    <4> = Technology Research
#    <5> = Minerals, Gas (Guardian/Devourer Aspect)
#
# * Starcraft will ignore all color tags after this.
#----------------------------------------------------
"""

DEF_DECOMPILE = ''.join([chr(x) for x in range(32)]) + '#<>'

def compile_string(string):
	def special_chr(o):
		c = int(o.group(1))
		if -1 > c or 255 < c:
			return o.group(0)
		return chr(c)
	return re.sub('<(\d+)>', special_chr, string)

def decompile_string(string, exclude='', include=''):
	def special_chr(o):
		return '<%s>' % ord(o.group(0))
	decompile = DEF_DECOMPILE + include
	if exclude:
		decompile = re.sub('[%s]' % re.escape(exclude),'',decompile)
	return re.sub('([%s])' % decompile, special_chr, string)

class TBL():
	def __init__(self):
		self.strings = []
		self.c = 0

	def load_file(self, file):
		data = load_file(file, 'TBL')
		extended = str(file).endswith(".tblex")
		format = '<I' if extended else '<H'

		try:
			n = struct.unpack(format, data[:4] if extended else data[:2])[0]
			offsets = struct.unpack('<%sI' % n if extended else '<%sH' % n, data[4:4+4*n] if extended else data[2:2+2*n])
			findlen = list(offsets) + [len(data)]
			findlen.sort(reverse=True)
			lengths = {}
			for i in xrange(1,len(findlen)):
				start = findlen[i]
				if not start in lengths:
					end = findlen[i-1]
					lengths[start] = end-start
			strings = []
			for i in xrange(len(offsets)):
				o = offsets[i]
				l = lengths[o]
				strings.append(data[o:o+l].decode('latin-1'))
			self.strings = strings
		except:
			raise PyMSError('Load',"Unsupported TBL file '%s', could possibly be corrupt" % file)

	def interpret(self, file):
		try:
			f = open(file,'r')
			data = f.readlines()
			f.close()
		except:
			raise PyMSError('Interpreting',"Could not load file '%s'" % file)
		strings = []
		for n,l in enumerate(data):
			line = l.split('#',1)[0]
			if line:
				if (len(strings) == 65536):
					raise PyMSError('Interpreting',"There are too many string entries (max entries is 65536)")
				s = compile_string(line.rstrip('\r\n'))
				strings.append(s)
		self.strings = strings

	def compile(self, file):
		try:
			f = AtomicWriter(file, 'wb')
		except:
			raise PyMSError('Compile', "Could not load file '%s'" % file)

		extended = str(file).endswith(".tblex")
		try:
			o = 4 + 4 * len(self.strings) if extended else 2 + 2 * len(self.strings)
			format = '<I' if extended else '<H'

			header = bytearray(struct.pack(format, len(self.strings)))
			data = bytearray()
			for s in self.strings:
				if not s.endswith('\x00'):
					s += '\x00'
				header += struct.pack(format, o)
				data += bytearray(s, 'latin-1')
				o += len(s)
			f.write(header + data)
			f.close()
		except:
			f.close()
			if not extended:
				return "You have probably reached the limit of standard format, please use extended format instead."
			else:
				return "You have probably reached the limit of extended format."
		return None


	def decompile(self, file, ref=False):
		try:
			f = AtomicWriter(file, 'w')
		except:
			raise PyMSError('Decompile',"Could not load file '%s'" % file)
		if ref:
			f.write(TBL_REF)
		for s in self.strings:
			f.write(decompile_string(s) + '\n')
		f.close()

#t = TBL()
#t.load_file('Data\stat_txt.tbl')
#t.decompile('test.txt')
# t.interpret('test.txt')
# t.compile('test.tbl')
# t.compile('test.tbl')
# o = open('out.txt','w')
# def getord(o):
   # return '<%s>' % ord(o.group(0))
# for s in t.strings:
   # o.write(re.sub('([\x00\x01\x02\x03\x04\x05\x06\x07\x08<>])', getord, s) + '\n')