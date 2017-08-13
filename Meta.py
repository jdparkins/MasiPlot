# Dictionaries and other globals and definitions for ease-of-use

# Currently only using molec_id, local_iso_id, nu, and sw for stick-plot phase
# Dictionary will expand as more parameters become relevant to development stage
PARAMETERS = {
	"molec_id": 0,
	"local_iso_id": 1,
	"nu": 2,
	"sw": 3
}

# Only H2O and O2 in use for testing
# Dictionary will expand as more molecules and their attributes become relevant to development stage
MOLECULES = {
	"H2O": {
		"name": "H2O",
		"M": 1,
		"Imax": 6
	},
	"O3": {
		"name": "O3"

	},
	"O2": {
		"name": "O2",
		"M": 7,
		"Imax": 3
	}
}

MOLECULE_NUMBER = {
	1: {
		"name": "H2O",
		"printName": "$H_2O$"
	},

	7: {
		"name": "O2",
		"printName": "$O_2$"
	},

	20: {
		"name": "H2CO",
		"printName": "$H_2CO$"
	}
}
