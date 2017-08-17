# Testing file -- essentially a copy of MasiPlot.py to use for development, testing, and validation.
from Meta import *
from Utils import *
from Plots import *
from matplotlib import pyplot

lineSurvey(readFile('CO2.txt'), 1e-3)
