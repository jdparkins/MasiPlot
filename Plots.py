# File to contain all functions pertaining to generating plots

from matplotlib import pyplot as plt, ticker
import numpy as np
from Meta import *
from Utils import *


# -------------------------------------
# ---------- PLOT GENERATORS ----------
# -------------------------------------

# Generate line survey
def lineSurvey(table, cutoff):
	# TODO: Interactive zoom and pan
	# TODO: Show attributes on mouseover
	# TODO: Add supplemental axis label to indicate wavelength
	# TODO: Annotations for T, P, species, and cutoff
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
	fig = plt.figure()
	fig.set_size_inches(12, 6)
	ax = fig.add_subplot(1, 1, 1)
	ax.set_yscale('log')
	plt.plot(nu, S)
	mean_nu = np.mean(nu)
	mean_S = np.mean(S)
	std_nu = np.std(nu)
	std_S = np.std(S)
	# Scale to x +- 0.1 sigma, y from 0 to max sw + 0.1 sigma
	plt.axis([min(nu) - 0.1 * std_nu, max(nu) + 0.1 * std_nu, cutoff, 2 * max(S)])
	plt.title(r"{0}: {1:.0f} < $\nu$ < {2:.0f}".format(printName, min(nu), max(nu)))
	plt.xlabel(r'Frequency [cm$^{-1}$]')
	plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
	plt.ylabel(r'$\chi_i *$Linestrength, [$\frac{cm^{-2}}{atm}$]')
	plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0e'))
	# Stub for labelling if wanted
	# for i in range (0, len(S)):
	# 	if S[i] > 0:
	# 		plt.text(nu[i], S[i], '({0:.1f},{1:.3e})'.format(nu[i], S[i]), fontsize = 8)
	plt.show()


# ---------------------------------
# ---------- CONVERSIONS ----------
# ---------------------------------

# Convert list of transition intensities from HITRAN units (cm^-1/molecule-cm^2) to linestrengths in cm^-2/atm per SP
def getLineStrength(ara):
	T0 = 300  # HITRAN T0 is 296 k, SP shows at 300 k
	for i in range(0, len(ara)):
		S = (1 / T0) * (7.34e21 * ara[i])  # This conversion is pretty greasy, but it's good to within +- 1.0%
		ara[i] = S


# Convert array of wavenumbers (cm^-1) to wavelengths (mu-m)
def convertToLambda(ara):
	lambdaList = []
	for i in range(0, len(ara)):
		lambdaList.insert(i, 10000 / ara[i])
	return lambdaList


# -------------------------------
# ---------- UTILITIES ----------
# -------------------------------

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
