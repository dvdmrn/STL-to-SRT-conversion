"""
	Compiles a windows exe using py2exe
"""

from distutils.core import setup
import py2exe
  
setup(console=['STLconvert.py'])