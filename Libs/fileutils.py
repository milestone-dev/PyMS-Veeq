from utils import *
from tkMessageBox import *

def isDefaultFile(path):
	path = path.replace("/", "\\")
	base_path = os.path.join(BASE_DIR, 'Libs', 'MPQ')
	return base_path in path

def overwriteFile(parent, path):
	if isDefaultFile(path):
		filename = re.sub(r".*[\\/](.*)", r"\1", path);
		return askquestion(parent=parent, title='Overwrite default file?', message="Do you want to overwrite default file '%s'?" % filename, default=OK, type=OKCANCEL) == "ok"
	return True

class BadFile:
	def __init__(self, file):
		self.file = file

	def __str__(self):
		return self.file

	def __nonzero__(self):
		return False

def load_file(file, file_type='file', mode='rb'):
	try:
		if isstr(file):
			f = open(file,mode)
		else:
			f = file
		data = f.read()
	except:
		name = ''
		if isstr(file):
			name = " '%s'" % file
		elif isinstance(file, BadFile):
			name = " '%s'" % file.file
		raise PyMSError('Load',"Could not load %s%s" % (file_type, name))
	finally:
		try:
			f.close()
		except:
			pass
	return data