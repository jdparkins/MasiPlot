from PyQt5 import QtWidgets

import Meta
import UIDesign
import Utils


class GUI(QtWidgets.QMainWindow, UIDesign.Ui_Masiplot):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# --------------------------
		# ----- INITIALISATION -----
		# --------------------------
		self.speciesField.addItems(Meta.MOLECULE_NAME.keys())  # Set keys for combination box
		self.tField.setText('300')  # Default value for temperature field
		self.pField.setText('1')  # Default value for pressure field
		self.nuMinField.setText('0')  # Default value for nu_min field
		self.nuMaxField.setText('5000')  # Default value for nu_max field
		self.cutoffField.setText('1.0e-3')
		self.plotType = 0

		# --------------------------
		# ------- FUNCTIONS --------
		# --------------------------
		self.lineSurveyBtn.clicked.connect(self.updateLSPlot)  # On button click, update plot with LineSurvey
		self.clearBtn.clicked.connect(self.clearPlot)
		self.exportCSVBtn.clicked.connect(self.export)

	# Update mplwidget with current parameters
	def updateLSPlot(self):
		self.plotType = 1
		molec_name, T, p, nuMin, nuMax, cutoff = self.getParams()  # Get current parameters
		self.mplwidget.updatePlot(molec_name, nuMin, nuMax, T, p, cutoff)  # Update line survey with current parameters

	# Get parameters from input fields
	def getParams(self):
		molec_name = str(self.speciesField.currentText())
		T = int(self.tField.text())
		P = int(self.pField.text())
		nuMin = int(self.nuMinField.text())
		nuMax = int(self.nuMaxField.text())
		cutoff = float(self.cutoffField.text())
		return molec_name, T, P, nuMin, nuMax, cutoff

	def clearPlot(self):
		self.mplwidget.clearPlot()

	def export(self):
		filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
		molec_name, T, p, nuMin, nuMax, cutoff = self.getParams()  # Get current parameters

		if self.plotType == 0:
			pass
		elif self.plotType == 1:
			Utils.exportCSV_Linestrength(filename, molec_name, T, p, nuMin, nuMax, cutoff)
		elif self.plotType == 2:
			Utils.exportCSV_Absorption(filename, molec_name, T, p, nuMin, nuMax, cutoff)
		elif self.plotType == 3:
			Utils.exportCSV_Emission(filename, molec_name, T, p, nuMin, nuMax, cutoff)
		elif self.plotType == 4:
			Utils.exportCSV_BlackBody(filename, molec_name, T, p, nuMin, nuMax, cutoff)


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Masiplot = GUI()
	# ui = UIDesign.Ui_Masiplot()
	# ui.setupUi(Masiplot)
	Masiplot.show()
	app.exec_()
