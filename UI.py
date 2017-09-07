from PyQt5 import QtWidgets

import Meta
import UIDesign


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

		# --------------------------
		# ------- FUNCTIONS --------
		# --------------------------
		self.lineSurveyBtn.clicked.connect(self.updateLSPlot)   # On button click, update plot with LineSurvey
		self.clearBtn.clicked.connect(self.clearPlot)

	# Update mplwidget with current parameters
	def updateLSPlot(self):
		molec_name, T, P, nuMin, nuMax = self.getParams()   # Get current parameters
		self.mplwidget.updatePlot(molec_name, nuMin, nuMax) # Update line survey with current parameters

	# Get parameters from input fields
	def getParams(self):
		molec_name = str(self.speciesField.currentText())
		T = int(self.tField.text())
		P = int(self.pField.text())
		nuMin = int(self.nuMinField.text())
		nuMax = int(self.nuMaxField.text())
		return molec_name, T, P, nuMin, nuMax

	def clearPlot(self):
		self.mplwidget.clearPlot()


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Masiplot = GUI()
	# ui = UIDesign.Ui_Masiplot()
	# ui.setupUi(Masiplot)
	Masiplot.show()
	app.exec_()
