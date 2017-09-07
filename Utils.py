# File for utility methods to keep main clean
import time

from LineItem import *
from Meta import *


# -----------------------------
# ---------- FILE IO ----------
# -----------------------------

# Initial DB read and import to array LOCAL_DB
def readDB():
	results = []
	startTime = time.time()
	with open("./data/SimpleDB.out", "r") as fileIn:
		for line in fileIn:
			results.append(generateLineItem(splitLine(line.strip())))
	print("Local database parsed in {0:.2f} seconds".format(getRunTime(startTime)))
	return results


# Read specific file
def readFile(filename):
	results = []
	with open("./data/" + filename, "r") as fileIn:
		for line in fileIn:
			results.append(generateLineItem(splitLine(line.strip())))
	return results


# Print query to a file
def printToFile(ara, filename):
	fileOut = open("./data/" + filename + ".txt", "w")
	for i in range(0, len(ara)):
		for j in range(0, 4):
			fileOut.write("%s " % ara[i][j])
		fileOut.write("\n")


# Break large DB into smaller DB by HITRAN molecule ID
def createSubDB(originalDB, molec_id):
	results = searchDB_ID(originalDB, molec_id, 1)
	printToFile(results, MOLECULE_NUMBER[molec_id]["formula"])
	print("{0}:{1} successfully added".format(molec_id, MOLECULE_NUMBER[molec_id]['formula']))


# Create sub DB for all molecule species most common isotopes (i.e. (I, 1))
def fetchAllMolecules():
	baseDB = readDB()
	print("Base DB read.")
	for key in MOLECULE_NUMBER:
		createSubDB(baseDB, key)


# -----------------------------
# ---------- QUERIES ----------
# -----------------------------

# Search LOCAL_DB by molec_id and local_iso_id
def searchDB_ID(DB, M, I):
	startTime = time.time()
	lineCount = 1
	lineTotal = len(DB)
	results = []
	for i in range(0, lineTotal):
		if DB[i][0] == M and DB[i][1] == I:
			results.append(DB[i])
		else:
			pass
	return results


# Expanded search to cover nu range
def searchDB_NU(DB, nuMin, nuMax):
	startTime = time.time()
	lineCount = 1
	lineTotal = len(DB)
	results = []
	for i in range(0, lineTotal):
		if nuMin < DB[i][2] < nuMax:
			results.append(DB[i])
		else:
			pass
	return results


# ---------------------------------------
# ---------- DATA MANIPULATION ----------
# ---------------------------------------

# Quick and dirty array printer
def printArray(ara):
	for i in range(0, len(ara)):
		print(ara[i])


# Split file lines into tokenized strings
def splitLine(line):
	tokens = line.split()
	for i in range(0, len(tokens)):
		tokens[i].strip('\t')
	return tokens


# Generate LineItem from splitLine()
def generateLineItem(ara):
	return LineItem(ara[0], ara[1], ara[2], ara[3])


# Fetch specified columns of array as individual lists
def getColumns(ara, ParameterNames):
	columns = []
	for par_name in ParameterNames:
		if par_name in PARAMETERS.keys():
			tempCol = []
			for i in range(0, len(ara)):
				tempCol.append(ara[i][PARAMETERS[par_name]])
			columns.append(tempCol)
		else:
			print("{0} is an invalid parameter.".format(par_name))
			pass
	return columns


# -----------------------------
# ---------- TESTING ----------
# -----------------------------

# Utility function used for fast testing of new methods -- ignore
def readNLines(n, filename):
	results = []
	with open("./data/" + filename, "r") as fileIn:
		for i in range(0, n):
			line = fileIn.__next__()
			results.append(generateLineItem(splitLine(line.strip())))
	return results


# Read small test database for testing
def readTest():
	results = []
	with open("./data/CO_NU2195-2220.txt", "r") as fileIn:
		for line in fileIn:
			results.append(generateLineItem(splitLine(line.strip())))
	return results


# Function for testing -- ignore
def getFileLength(filename):
	with open("./data/" + filename, "r") as fileIn:
		content = fileIn.readlines()
	return len(content)


# Function for testing and analysis -- ignore
def getRunTime(startTime):
	return float((time.time() - startTime))
