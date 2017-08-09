# File for utility methods to keep main clean
import time

from matplotlib import pyplot
from numpy import *
from LineItem import *
from Meta import *


# Initial DB read and import to array LOCAL_DB
def readDB():
	results = []
	startTime = time.time()
	with open("./data/SimpleDB.out", "r") as fileIn:
		for line in fileIn:
			results.append(generateLineItem(splitLine(line.strip())))
	print("Local database parsed in {0:.2f} seconds".format(getRunTime(startTime)))
	return results


# Utility function used for fast testing of new methods -- ignore
def readFastDB():
	results = []
	startTime = time.time()
	with open("./data/SimpleDB.out", "r") as fileIn:
		for i in range(0, 100):
			line = fileIn.__next__()
			results.append(generateLineItem(splitLine(line.strip())))
	return results


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
def searchDB_NU(DB, molID, isoID, nuMin, nuMax):
	startTime = time.time()
	lineCount = 1
	lineTotal = len(DB)
	results = []
	for i in range(0, lineTotal):
		if DB[i][0] == molID and DB[i][1] == isoID and nuMin < DB[i][2] < nuMax:
			results.append(DB[i])
		else:
			pass
	return results


# Fetches specified columns of array -- used to pick data for plotting
def getColumns(ara, ParameterNames):
	columns = []
	for par_name in ParameterNames:
		tempCol = []
		for i in range(0, len(ara)):
			tempCol.append(ara[i][PARAMETERS[par_name]])
		columns.append(tempCol)
	return columns


def getStickXY(TableName):
	"""
    Get X and Y for fine plotting of a stick spectrum.
    Usage: X,Y = getStickXY(TableName).
    """
	cent, intens = getColumns(TableName, ('nu', 'sw'))
	n = len(cent)
	cent_ = zeros(n * 3)
	intens_ = zeros(n * 3)
	for i in range(n):
		intens_[3 * i] = 0
		intens_[3 * i + 1] = intens[i]
		intens_[3 * i + 2] = 0
		cent_[(3 * i):(3 * i + 3)] = cent[i]
	return cent_, intens_


def stickPlot(DB):
	x, y = getStickXY(DB)
	pyplot.plot(x, y)
	pyplot.show()

# Function for testing -- ignore
def getFileLength(filename):
	with open("./data/" + filename, "r") as fileIn:
		content = fileIn.readlines()
	return len(content)


# Function for testing and analysis -- ignore
def getRunTime(startTime):
	return float((time.time() - startTime))


# Quick and dirty array printer
def printArray(ara):
	for i in range(0, len(ara)):
		print(ara[i])


# Method to split file lines into tokenized strings
def splitLine(line):
	tokens = line.split()
	for i in range(0, len(tokens)):
		tokens[i].strip('\t')
	return tokens


# Method to generate LineItem from splitLine()
def generateLineItem(ara):
	return LineItem(ara[0], ara[1], ara[2], ara[3])
