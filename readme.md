# PyMS
PyMS is a cross platform BroodWar modding suite written using [Python](http://www.python.org). PyMS contains 15 programs to edit most of the file types you will encounter while modding. This modding suite was originally created by poiuy_qwert and has since been maintained by Neiv, iquare, Veeq7, DarkenedFantasies, and Pr0nogo. This repository is home to the final updates the suite will see from us before a new modding suite enters development.

## Table of Contents
1. [Installation]()
1. [Issues]()
1. [Analytics]()
1. [Programs]()
   * [PyAI]()
   * [PyBIN]()
   * [PyDAT]()
   * [PyFNT]()
   * [PyGOT]()
   * [PyGRP]()
   * [PyICE]()
   * [PyLO]()
   * [PyMPQ]()
   * [PyPAL]()
   * [PyPCX]()
   * [PySPK]()
   * [PyTBL]()
   * [PyTILE]()
   * [PyTRG]()


## Installation
1. **Install Python.** You should get the latest Python 2.7.x, currently that is [Python 2.7.12](https://www.python.org/downloads/release/python-2712/)
2. **Install PILLOW.** Use PIP, the Python package manager, to [install PILLOW](https://pillow.readthedocs.io/en/latest/installation.html#basic-installation) (PIL will also work)
3. **Download PyMS.** Always get the most up to date PyMS from [gitlab](https://gitlab.com/Pr0nogo/pyms-ngs/-/tree/master). If you are updating PyMS, you can keep your settings files located in the Settings folder and any modifications you've made to unitdef.txt.

## Issues/Feedback
If you run into any issues with the programs, or have any feedback to improve the programs, please do one of the following:
1. Create an issue [here on gitlab](https://gitlab.com/Pr0nogo/pyms-ngs/-/issues)
1. Contact us on [Discord](https://discordapp.com/invite/s5SKBmY)
1. Email [Pr0nogo](mailto:pronogo@hotmail.com) or [Veeq7](mailto:veeq72@gmail.com)

Please include as much information as possible. If you are reporting an issue, please include:
* The version of the program you had issues with (you can check in Libs\versions.json)
* The OS you are running on
* The error message or crash logs. If the program crashed without an error dialog, you can check in the Libs\Logs\ folder for the program's log file

## Analytics
At the moment PyMS only tracks the launch of PyMS programs, anonamously and with no sensitive information sent. An example of the data sent in these analytics calls:

```
{
  "an": "PyGRP",
  "av": "4.0.0",
  "cd": "PyGRP",
  "cd1": "1.2.3",
  "cd2": "2.7.10",
  "cd3": "darwin",
  "cd4": "10.12.6",
  "cd5": 64,
  "cid": "bd32dccd-13be-4027-86eb-8a3fc11c61e7",
  "t": "screenview",
  "tid": "UA-########-#",
  "v": "1"
}
```

Even though the analytics is anonamous and has no sensitive information, you can still disable analytics by editing "Settings/PyMS.txt", and setting the "allow" key under "analytics" to be False.

## Programs
PyMS contains 16 programs to edit most of the file types you will encounter while modding.

### PyAI
PyAI is used for editing AI .bin files.

### PyBIN
PyBIN is used for editing dialog .bin files.

### PyDAT
PyDAT is used for editing the various .dat files.

### PyFNT
PyFNT is used for converting .fnt Font files to and from .bmp files.

### PyGOT
PyGOT is used for editing the Game Template .got files.

### PyGRP
PyGRP is used for editing various graphics in .grp files.

### PyICE
PyICE is used for editing the graphics animation script .bin files.

### PyLO
PyLO is used for editing the various offset .lo? files.

### PyMPQ
PyMPQ is used for editing .mpq files.

### PyPAL
PyPAL is used for editing the various image palette files (.pal, .wpe, etc.)

### PyPCX
PyPAL is used for converting .pcx files to and from .bmp files.

### PySPK
PySPK is used for editing the space paralax .spk files.

### PyTBL
PyTBL is used for editing the strings .tbl files.

### PyTILE
PyTILE is used for editing the tileset files (.cv5, .vx4, .vf4, .vr4, .dddata)

### PyTRG
PyTRG is used for editing triggers (.trg files)
