import sys
import os, os.path

# Install default path for modules

mainpath=sys.path.pop(0)
mainpath=os.path.abspath(mainpath)
site_packages = os.path.join(mainpath,"site-packages")
sys.path.insert(0,site_packages)
sys.path.insert(0,mainpath)

# Make jython somewhat compartible to CPython-3.X

from six import *

# place here Your code and imports
