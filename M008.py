# Module
# Andere Skripte/Skriptsammlungen hier einbinden

# import
# Importiert aus einem anderen Skript Codeteilen
# WICHTIG: Wenn ein Skript importiert wird, wird es immer vollständig ausgeführt
# Auf der Wurzelebene sind nur Variablen-, Funktions- und Klassendefinitionen erlaubt
import M006
M006.halloWelt()  # Hier kann auf Code von M006 zugegriffen werden

import e3series as e3  # Mit as kann ein Paket "umbenannt" werden
print(e3.Application)

# from import
# Importiert aus einem anderen Skript bestimmte Member, und bindet diese direkt in das Skript ein
# -> kein Prefix bei Verwendung von Membern aus dem anderen Skript nötig
# WICHTIG: Wenn ein Skript importiert wird, wird es immer vollständig ausgeführt
# Auf der Wurzelebene sind nur Variablen-, Funktions- und Klassendefinitionen erlaubt
from M006 import halloWelt
halloWelt()

from M006 import *  # Importiert alle Member direkt in das Skript
halloWelt()
addiere(2, 3)

from e3series import Application
print(Application)

###########################################

# Der Modul Suchpfad
import sys
from sys import path

for p in sys.path:
	print(p)

# 1. Selbes Projekt
# 2. Globale Pakete
# 3. Extern installierte Pakete (.venv)
# 4. Eigene Pfade (mit append)
sys.path.append("C:\\Users\\lk3\\Desktop")
import xyz

###########################################

# Externe Pakete
# Zwei Optionen
# - Python Packages
# - Terminal (über pip)

import pandas

# in .venv/Lib/site-packages werden alle externen Pakete abgelegt
# Die .venv kann in weiterer Folge auf beliebig vielen Rechnern kopiert werden

###########################################

# Die Main-Methode
# Eine einfache if-Anweisung, die bei direktem Start des Skriptes ausgeführt wird
# Beim Import wird dieser Code nicht ausgeführt

# __name__
# Enthält entweder den Namen des Skriptes selbst (bei einem Import)
# Oder __main__, bei einem direkten Start
print(__name__)

if __name__ == "__main__":
	print("Direkter Start")

###########################################

# Pakete
# Einfache Ordner
from M008b import M008b
M008b.hallo()