# Testing file -- essentially a copy of MasiPlot.py to use for development, testing, and validation.
from Meta import *
from Utils import *

# Read local database text file in to array
LOCAL_DB = readFastDB()

search = searchDB_ID(LOCAL_DB, MOLECULES["O2"]["M"], 1)
cols = getColumns(search, ("nu", "sw"))
printArray(search)
printArray(cols)
print("Done")
