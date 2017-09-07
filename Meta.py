# Dictionaries and other globals and definitions for ease-of-use

# Currently only using molec_id, local_iso_id, nu, and sw for stick-plot phase
# Dictionary will expand as more parameters become relevant to development stage
PARAMETERS = {
	"molec_id": 0,
	"local_iso_id": 1,
	"nu": 2,
	"sw": 3,
	"s" : 3
}

# Only H2O and O2 in use for testing
# Dictionary will expand as more molecules and their attributes become relevant to development stage
MOLECULE_NAME = {
	"H2O": {"molec_id": 1, "name": "Water"},
	"CO2": {"molec_id": 2, "name": "Carbon Dioxide"},
	"O3": {"molec_id": 3, "name": "Ozone"},
	"N2O": {"molec_id": 4, "name": "Nitrous Oxide"},
	"CO": {"molec_id": 5, "name": "Carbon Monoxide"},
	"CH4": {"molec_id": 6, "name": "Methane"},
	"O2": {"molec_id": 7, "name": "Molecular Oxygen"},
	"NO": {"molec_id": 8, "name": "Nitric Oxide"},
	"SO2": {"molec_id": 9, "name": "Sulfur Dioxide"},
	"NO2": {"molec_id": 10, "name": "Nitrogen Dioxide"},
	"NH3": {"molec_id": 11, "name": "Ammonia"},
	"HNO3": {"molec_id": 12, "name": "Nitric Acid"},
	"OH": {"molec_id": 13, "name": "Hydroxyl Radical"},
	"HF": {"molec_id": 14, "name": "Hydrogen Fluoride"},
	"HCl": {"molec_id": 15, "name": "Hydrogen Chloride"},
	"HBr": {"molec_id": 16, "name": "Hydrogen Bromide"},
	"HI": {"molec_id": 17, "name": "Hydrogen Iodide"},
	"ClO": {"molec_id": 18, "name": "Chlorine Monoxide"},
	"OCS": {"molec_id": 19, "name": "Carbonyl Sulfide"},
	"H2CO": {"molec_id": 20, "name": "Formaldehyde"},
	"HOCl": {"molec_id": 21, "name": "Hypochlorous Acid"},
	"N2": {"molec_id": 22, "name": "Molecular Nitrogen"},
	"HCN": {"molec_id": 23, "name": "Hydrogen Cyanide"},
	"CH3Cl": {"molec_id": 24, "name": "Methyl Chloride"},
	"H2O2": {"molec_id": 25, "name": "Hydrogen Peroxide"},
	"C2H2": {"molec_id": 26, "name": "Acetylene"},
	"C2H6": {"molec_id": 27, "name": "Ethane"},
	"PH3": {"molec_id": 28, "name": "Phosphine"},
	"COF2": {"molec_id": 29, "name": "Carbonyl Fluoride"},
	"SF6": {"molec_id": 30, "name": "Sulfur Hexafluoride"},
	"H2S": {"molec_id": 31, "name": "Hydrogen Sulfide"},
	"HCOOH": {"molec_id": 32, "name": "Formic Acid"},
	"HO2": {"molec_id": 33, "name": "Hydroperoxyl Radical"},
	"O": {"molec_id": 34, "name": "Oxygen Atom"},
	"ClONO2": {"molec_id": 35, "name": "Chlorine Nitrate"},
	"NO+": {"molec_id": 36, "name": "Nitric Oxide Cation"},
	"HOBr": {"molec_id": 37, "name": "Hypobromous Acid"},
	"C2H4": {"molec_id": 38, "name": "Ethylene"},
	"CH3OH": {"molec_id": 39, "name": "Methanol"},
	"CH3Br": {"molec_id": 40, "name": "Methyl Bromide"},
	"CH3CN": {"molec_id": 41, "name": "Methyl Cyanide"},
	"CF4": {"molec_id": 42, "name": "Carbon Tetrafluoride"},
	"C4H2": {"molec_id": 43, "name": "Diacetylene"},
	"HC3N": {"molec_id": 44, "name": "Cyanoacetylene"},
	"H2": {"molec_id": 45, "name": "Molecular Hydrogen"},
	"CS": {"molec_id": 46, "name": "Carbon Monosulfide"},
	"SO3": {"molec_id": 47, "name": "Sulfur trioxide"},
	"C2N2": {"molec_id": 48, "name": "Cyanogen"},
	"COCl2": {"molec_id": 49, "name": "Phosgene"},

}

MOLECULE_NUMBER = {
	1: {"formula": "H2O", "name": "Water"},
	2: {"formula": "CO2", "name": "Carbon Dioxide"},
	3: {"formula": "O3", "name": "Ozone"},
	4: {"formula": "N2O", "name": "Nitrous Oxide"},
	5: {"formula": "CO", "name": "Carbon Monoxide"},
	6: {"formula": "CH4", "name": "Methane"},
	7: {"formula": "O2", "name": "Molecular Oxygen"},
	8: {"formula": "NO", "name": "Nitric Oxide"},
	9: {"formula": "SO2", "name": "Sulfur Dioxide"},
	10: {"formula": "NO2", "name": "Nitrogen Dioxide"},
	11: {"formula": "NH3", "name": "Ammonia"},
	12: {"formula": "HNO3", "name": "Nitric Acid"},
	13: {"formula": "OH", "name": "Hydroxyl Radical"},
	14: {"formula": "HF", "name": "Hydrogen Fluoride"},
	15: {"formula": "HCl", "name": "Hydrogen Chloride"},
	16: {"formula": "HBr", "name": "Hydrogen Bromide"},
	17: {"formula": "HI", "name": "Hydrogen Iodide"},
	18: {"formula": "ClO", "name": "Chlorine Monoxide"},
	19: {"formula": "OCS", "name": "Carbonyl Sulfide"},
	20: {"formula": "H2CO", "name": "Formaldehyde"},
	21: {"formula": "HOCl", "name": "Hypochlorous Acid"},
	22: {"formula": "N2", "name": "Molecular Nitrogen"},
	23: {"formula": "HCN", "name": "Hydrogen Cyanide"},
	24: {"formula": "CH3Cl", "name": "Methyl Chloride"},
	25: {"formula": "H2O2", "name": "Hydrogen Peroxide"},
	26: {"formula": "C2H2", "name": "Acetylene"},
	27: {"formula": "C2H6", "name": "Ethane"},
	28: {"formula": "PH3", "name": "Phosphine"},
	29: {"formula": "COF2", "name": "Carbonyl Fluoride"},
	30: {"formula": "SF6", "name": "Sulfur Hexafluoride"},
	31: {"formula": "H2S", "name": "Hydrogen Sulfide"},
	32: {"formula": "HCOOH", "name": "Formic Acid"},
	33: {"formula": "HO2", "name": "Hydroperoxyl Radical"},
	34: {"formula": "O", "name": "Oxygen Atom"},
	35: {"formula": "ClONO2", "name": "Chlorine Nitrate"},
	36: {"formula": "NO+", "name": "Nitric Oxide Cation"},
	37: {"formula": "HOBr", "name": "Hypobromous Acid"},
	38: {"formula": "C2H4", "name": "Ethylene"},
	39: {"formula": "CH3OH", "name": "Methanol"},
	40: {"formula": "CH3Br", "name": "Methyl Bromide"},
	41: {"formula": "CH3CN", "name": "Methyl Cyanide"},
	42: {"formula": "CF4", "name": "Carbon Tetrafluoride"},
	43: {"formula": "C4H2", "name": "Diacetylene"},
	44: {"formula": "HC3N", "name": "Cyanoacetylene"},
	45: {"formula": "H2", "name": "Molecular Hydrogen"},
	46: {"formula": "CS", "name": "Carbon Monosulfide"},
	47: {"formula": "SO3", "name": "Sulfur trioxide"},
	48: {"formula": "C2N2", "name": "Cyanogen"},
	49: {"formula": "COCl2", "name": "Phosgene"},

}
