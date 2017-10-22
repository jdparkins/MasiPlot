# File for utility methods to keep main clean
import time
import hapi
import math
import LineItem
import Meta
from scipy import constants
from PyQt5 import QtWidgets


# -----------------------------
# ---------- FILE IO ----------
# -----------------------------

# Initial DB read and import to array LOCAL_DB
def readDB():
	results = []
	with open("./data/_MAINDB.out", "r") as fileIn:
		for line in fileIn:
			results.append(generateLineItem(splitLine(line.strip())))
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
		for j in range(0, 6):
			fileOut.write("%s " % ara[i][j])
		fileOut.write("\n")


# Break large DB into smaller DB by HITRAN molecule ID
def createSubDB(originalDB, molec_id):
	results = searchDB_ID(originalDB, molec_id, 1)
	printToFile(results, Meta.MOLECULE_NUMBER[molec_id]["formula"])
	print("{0}:{1} successfully added".format(molec_id, Meta.MOLECULE_NUMBER[molec_id]['formula']))


# Create sub DB for all molecule species most common isotopes (i.e. (M, 1))
def fetchAllMolecules():
	baseDB = readDB()
	print("Base DB read.")
	for key in Meta.MOLECULE_NUMBER:
		createSubDB(baseDB, key)


def exportCSV_Linestrength(filename, molec_name, T, p, nuMin, nuMax, cutoff):
	table = searchDB_NU(readFile(molec_name + ".txt"), nuMin, nuMax)
	getLineStrength(table, T)
	getPressureShift(table, p)
	_nu, _S = getColumns(table, ('nu', 's'))
	_nu, _S = applyCutoff(_nu, _S, cutoff)
	fileOut = open(filename[0], "w")

	for i in range(0, len(_nu)):
		fileOut.write("{0}, {1}\n".format(_nu[i], _S[i]))
	fileOut.close()


def exportCSV_Absorption(filename, molec_name, T, p, nuMin, nuMax, cutoff):
	table = searchDB_NU(readFile(molec_name + ".txt"), nuMin, nuMax)


def exportCSV_Emission(filename, molec_name, T, p, nuMin, nuMax, cutoff):
	table = searchDB_NU(readFile(molec_name + ".txt"), nuMin, nuMax)


def exportCSV_BlackBody(filename, molec_name, T, p, nuMin, nuMax, cutoff):
	table = searchDB_NU(readFile(molec_name + ".txt"), nuMin, nuMax)


# -----------------------------
# ---------- QUERIES ----------
# -----------------------------

# Search LOCAL_DB by molec_id and local_iso_id
def searchDB_ID(DB, M, I):
	results = []
	for i in range(0, len(DB)):
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


# Generates and returns line item object from splitLine()
def generateLineItem(ara):
	return LineItem.LineItem(ara[0], ara[1], ara[2], ara[3], ara[4], ara[5])


# Fetch specified columns of array as individual lists
def getColumns(ara, ParameterNames):
	columns = []
	for par_name in ParameterNames:
		if par_name in Meta.PARAMETERS.keys():
			tempCol = []
			for i in range(0, len(ara)):
				tempCol.append(ara[i][Meta.PARAMETERS[par_name]])
			columns.append(tempCol)
		else:
			print("{0} is an invalid parameter.".format(par_name))
			pass
	return columns


# Calculate temperature-dependent intensity for all items in table and replace original values with calculated values
# Also, convert HITRAN units to SpectraPlot units
# TODO: Add error-checking for T < 0, T -> 0, T -> infty
# TODO: Create new method for converting units to clean-up method
def getLineStrength(ara, T):
	# HITRAN values native at T0 = 296k.
	# If T is 296, just convert units.
	if T == 296:
		# Convert intensity from HITRAN units  to SpectraPlot units
		# [cm^-1/molecule-cm^2] -> [cm^-2/atm]
		for i in range(0, len(ara)):
			Sj = (1 / T) * (7.34e21 * ara[i])
			ara[i] = Sj

	# Else, do the things.
	else:
		# Get and set constants.
		T0 = 296
		h = constants.h
		c = constants.c
		k = constants.k
		molec_id = ara[0][Meta.PARAMETERS["molec_id"]]
		QT0 = hapi.partitionSum(molec_id, 1, T0)
		QT = hapi.partitionSum(molec_id, 1, T)

		# Calculate S_j(T) for each S in data set and replace.
		for i in range(0, len(ara)):
			SjT0 = ara[i][Meta.PARAMETERS["s"]]
			Ej = ara[i][Meta.PARAMETERS["elower"]]
			v = ara[i][Meta.PARAMETERS["nu"]]
			Sj = (SjT0) * (QT0 / QT) * (math.exp(((-h * c * Ej) / k) * ((1 / T) - (1 / T0)))) * (
				(1 - (math.exp((-h * c * v) / (k * T)))) * (1 / (1 - (math.exp((-h * c * v) / (k * T0))))))
			ara[i][Meta.PARAMETERS["s"]] = Sj

		# Convert intensity from HITRAN units  to SpectraPlot units
		# [cm^-1/molecule-cm^2] -> [cm^-2/atm]
		for i in range(0, len(ara)):
			Sj = (1 / T) * (7.34e21 * ara[i][Meta.PARAMETERS["s"]])
			ara[i][Meta.PARAMETERS["s"]] = Sj


# Calculate pressure shift for wavenumbers
# TODO: Add error checking for p < 0, p -> infty
def getPressureShift(ara, p):
	# HITRAN provides vacuum wavenumbers
	# If pressure is zero, don't bother changing anything.
	if p == 0:
		pass

	# Otherwise, shift ze wavenumbers!
	else:
		for i in range(0, len(ara)):
			nu_ij = ara[i][Meta.PARAMETERS["nu"]]
			delta_air = ara[i][Meta.PARAMETERS["delta_air"]]
			nu_star_ij = nu_ij + (delta_air * p)
			ara[i][Meta.PARAMETERS["nu"]] = nu_star_ij


# Apply cutoff to restrict values based on cutoff value of a2 list
def applyCutoff(a1, a2, cut):
	_a1 = []
	_a2 = []
	for i in range(0, len(a2)):
		if float(a2[i]) > cut:
			_a1.append(a1[i])
			_a2.append(a2[i])
	a1.clear()
	a2.clear()
	return _a1, _a2


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
