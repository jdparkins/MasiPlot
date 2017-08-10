# This file is the main driver for MasiPlot
from Utils import *

# Read local database text file in to array
LOCAL_DB = readDB()

testDB = searchDB_ID(LOCAL_DB, 1, 1)
stickPlot(testDB)


# Call interface