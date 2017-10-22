# Testing for native HAPI import format functionality using CO2.data

import hapi

hapi.tableList()
hapi.select("H20")
nu = hapi.getColumn('H2O', 'nu')
