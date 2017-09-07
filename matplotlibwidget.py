from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import *

import Meta
import Utils
from Plots import *


class MatplotlibWidget(FigureCanvas):
	def __init__(self, parent=None, width=12, height=6, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.ax1 = fig.add_subplot(111)
		self.ax1.set_xlabel(r'Frequency [cm$^{-1}$]')
		self.ax1.set_ylabel(r'$\chi_i *$Linestrength, [$\frac{cm^{-2}}{atm}$]')
		self.ax1.set_yscale('log')

		self.ax2 = self.ax1.twiny()
		ax1Ticks = self.ax1.get_xticks()
		ax2Ticks = ax1Ticks
		self.ax2.set_xticks(ax2Ticks)
		self.ax2.set_xbound(self.ax1.get_xbound())
		self.ax2.set_xticklabels(tick_function(ax2Ticks))
		self.ax2.set_yscale('log')

		# fig.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
		# fig.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0e'))



		FigureCanvas.__init__(self, fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	# self.plot()

	# def plot(self):
	# 	# table = readFile("CO2.txt")
	# 	# col = getColumns(table, ("sw"))
	# 	# data = col
	# 	table = readFile("CO2.txt")
	# 	cutoff = 1e-3
	# 	printName = MOLECULE_NUMBER[table[0][0]]["formula"]
	# 	_nu, _S = getColumns(table, ('nu', 'sw'))
	# 	getLineStrength(_S)
	# 	_nu, _S = applyCutoff(_nu, _S, cutoff)
	# 	n = len(_nu)
	# 	nu = np.zeros(n * 3)
	# 	S = np.zeros(n * 3)
	# 	for i in range(n):
	# 		S[3 * i] = 0
	# 		S[3 * i + 1] = _S[i]
	# 		S[3 * i + 2] = 0
	# 		nu[(3 * i):(3 * i + 3)] = _nu[i]
	#
	# 	ax = self.figure.add_subplot(111)
	# 	ax.set_yscale('log')
	# 	ax.plot(nu, S)
	# 	std_nu = np.std(nu)
	# 	# Scale to x +- 0.1 sigma, y from 0 to max sw + 0.1 sigma
	# 	ax.axis([min(nu) - 0.1 * std_nu, max(nu) + 0.1 * std_nu, cutoff, 2 * max(S)])
	# 	ax.set_title(r"{0}: {1:.0f} < $\nu$ < {2:.0f}".format(printName, min(nu), max(nu)))
	# 	ax.set_xlabel(r'Frequency [cm$^{-1}$]')
	# 	self.figure.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
	# 	ax.set_ylabel(r'$\chi_i *$Linestrength, [$\frac{cm^{-2}}{atm}$]')
	# 	self.figure.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0e'))
	# 	self.draw()

	def updatePlot(self, molec_name, nuMin, nuMax):
		molec_id = Meta.MOLECULE_NAME[molec_name]['molec_id']
		table = self.fetchTable(molec_name, nuMin, nuMax)
		cutoff = 1e-3
		printName = MOLECULE_NUMBER[table[0][0]]["formula"]
		_nu, _S = getColumns(table, ('nu', 'sw'))
		getLineStrength(_S)
		_nu, _S = applyCutoff(_nu, _S, cutoff)
		n = len(_nu)
		nu = np.zeros(n * 3)
		S = np.zeros(n * 3)
		for i in range(n):
			S[3 * i] = 0
			S[3 * i + 1] = _S[i]
			S[3 * i + 2] = 0
			nu[(3 * i):(3 * i + 3)] = _nu[i]

		# Main Plot
		plot = self.figure.add_subplot(111)
		plot.plot(nu, S)
		self.draw()

		std_nu = np.std(nu)
		# Scale to x +- 0.1 sigma, y from 0 to max sw + 0.1 sigma
		#ax1.axis([min(nu) - 0.1 * std_nu, max(nu) + 0.1 * std_nu, cutoff, 2 * max(S)])
		#ax1.set_title(r"{0}: {1:.0f} < $\nu$ < {2:.0f}".format(printName, min(nu), max(nu)), y = 1.10)
	def fetchTable(self, molec_name, nuMin, nuMax):
		table = Utils.searchDB_NU(readFile(molec_name + ".txt"), nuMin, nuMax)
		return table


	def clearPlot(self):
		self.figure.clf()
		self.axes = self.figure.add_subplot(111)
		self.axes.set_yscale('log')
		self.draw()

def tick_function(X):
	c = 3.0e8
	V = c/X
	return ["%.0e" % z for z in V]
