# Testing file -- essentially a copy of MasiPlot.py to use for development, testing, and validation.
from Meta import *
from Utils import *
from matplotlib import pyplot

# Read local database text file in to array
LOCAL_DB = readDB()
printArray(LOCAL_DB)
