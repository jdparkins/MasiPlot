from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import ticker
import numpy as np

import Meta
import Utils


class MatplotlibWidget(FigureCanvas):
	def __init__(self, parent=None, width=14, height=10, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		FigureCanvas.__init__(self, fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def updatePlot(self, molec_name, nuMin, nuMax, T, p, cutoff):
		molec_id = Meta.MOLECULE_NAME[molec_name]['molec_id']
		table = self.fetchTable(molec_name, nuMin, nuMax)
		printName = Meta.MOLECULE_NUMBER[table[0][0]]["formula"]
		Utils.getLineStrength(table, T)
		Utils.getPressureShift(table, p)
		_nu, _S = Utils.getColumns(table, ('nu', 's'))
		_nu, _S = Utils.applyCutoff(_nu, _S, cutoff)
		n = len(_nu)
		nu = np.zeros(n * 3)
		S = np.zeros(n * 3)
		std_nu = np.std(nu)
		for i in range(n):
			S[3 * i] = 0
			S[3 * i + 1] = _S[i]
			S[3 * i + 2] = 0
			nu[(3 * i):(3 * i + 3)] = _nu[i]

		# Main Plot
		plot = self.figure.add_subplot(111)
		plot.plot(nu, S)
		plot.axes.set_yscale('log')
		plot.axes.set_ylabel(r'$\chi_i *$Linestrength, [$\frac{cm^{-2}}{atm}$]')
		plot.axes.set_xlabel(r'Wavenumber [cm$^{-1}$]')
		self.figure.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.e'))
		self.figure.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.f'))

		self.draw()

	# Scale to x +- 0.1 sigma, y from 0 to max sw + 0.1 sigma
	# ax1.axis([min(nu) - 0.1 * std_nu, max(nu) + 0.1 * std_nu, cutoff, 2 * max(S)])
	# ax1.set_title(r"{0}: {1:.0f} < $\nu$ < {2:.0f}".format(printName, min(nu), max(nu)), y = 1.10)
	def fetchTable(self, molec_name, nuMin, nuMax):
		table = Utils.searchDB_NU(Utils.readFile(molec_name + ".txt"), nuMin, nuMax)
		return table

	def clearPlot(self):
		self.figure.clf()
		self.draw()
