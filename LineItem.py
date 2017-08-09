# LineItem class represents a line read-in from the local text database
class LineItem(object):
	# Constructor
	def __init__(self, molec_id=0, local_iso_id=1, nu=0.0, sw=0.0):
		self.molec_id = int(molec_id)
		self.local_iso_id = int(local_iso_id)
		self.nu = float(nu)
		self.sw = float(sw)

	# __getitem__ to make class iterable
	def __getitem__(self, key):
		if key == 0:
			return self.molec_id
		elif key == 1:
			return self.local_iso_id
		elif key == 2:
			return self.nu
		elif key == 3:
			return self.sw
		else:
			return "Invalid key value"

	# "toString" method
	# Default format is all attributes separated by tabs
	def __str__(self):
		return str(self.molec_id) + "\t" + str(self.local_iso_id) + "\t" + str(self.nu) + "\t" + str(self.sw)
