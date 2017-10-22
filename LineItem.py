# LineItem class represents a line read-in from the local text database
class LineItem(object):
	# Constructor
	def __init__(self, molec_id=0, local_iso_id=1, nu=0.0, s=0.0, elower=0.0, delta_air=0.0):
		self.molec_id = int(molec_id)
		self.local_iso_id = int(local_iso_id)
		self.nu = float(nu)
		self.s = float(s)
		try:
			self.elower = float(elower)
		except ValueError:
			self.elower = 0.0
		self.delta_air = float(delta_air)

	# __getitem__ to make class iterable
	def __getitem__(self, key):
		if key == 0:
			return self.molec_id
		elif key == 1:
			return self.local_iso_id
		elif key == 2:
			return self.nu
		elif key == 3:
			return self.s
		elif key == 4:
			return self.elower
		elif key == 5:
			return self.delta_air
		else:
			return "Invalid key value"

	# __setitem__ to support item assignment
	def __setitem__(self, key, value):
		if key == 2:
			self.nu = value
		elif key == 3:
			self.s = value
		else:
			return "Invalid key value"

	# "toString" method
	# Default format is all attributes separated by tabs
	def __str__(self):
		return str(self.molec_id) + "\t" + str(self.local_iso_id) + "\t" + str(self.nu) + "\t" + str(
			self.s) + "\t" + str(self.elower)
