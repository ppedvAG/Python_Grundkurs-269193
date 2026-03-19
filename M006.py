# Funktionen
# Code wiederverwenden
# Code in Funktionen speichern, und über den Namen der Funktion den Code ausführen
from babel.messages.pofile import denormalize


# Syntax: def <Name>(): <Codeblock>
def halloWelt():
	print("Hallo")
	print("Welt")

halloWelt()  # Ab hier kann die Funktion verwendet werden
halloWelt()
halloWelt()

##################################

# Parameter
# Daten mitgeben
# Die Funktion soll etwas machen, anhand von den eingegebenen Daten
def hallo(name):
	print(f"Hallo {name}")

hallo("Max")  # Bei Verwendung dieser Funktion müssen jetzt Daten mitgegeben werden
hallo(123)  # Hier können beliebige Daten mitgegeben werden

# Typempfehlung
# Bei einem Parameter einen Hinweis geben, was hier erwartet wird
def hallo(name: str):
	print(f"Hallo {name}")

hallo("Max")
hallo(456)

# User davon abhalten mit einer Zahl weiterzumachen -> Typvergleich
def hallo(name: str):
	if type(name) == str:
		print(f"Hallo {name}")
	else:
		print("Name muss ein Text sein!")

hallo("Max")
hallo(456)

# Mehrere Typempfehlungen
# Mit einem senkrechten Strich ( | ) können mehrere Empfehlungen gemacht werden
def addiere(x: int | float, y: int | float):
	print(f"{x} + {y} = {x + y}")

addiere(2, 3)
addiere(3.4, 6.7)

##################################

# Rückgabewerte
# Daten/Ergebnisse an den User zurückgeben
# Beispiele: max, str.count, ...

liste = [1, 2, 3, 4]
m = max(liste)  # Das Ergebnis von max wird hier in der Variable m gefangen
print(f"Der höchste Wert ist {m}")

def addiere2(x: int, y: int):
	print(f"{x} + {y} = {x + y}")
	return x + y  # Über return wird ein Wert an den User zurückgegeben
	print()  # Die return Funktion "blockiert" dieses print-Statement

summe = addiere2(3, 4)  # In summe wird die Summe stehen (7)
print(summe)

##################################

# Default Parameter
# Parameter mit einem Standardwert versehen
# Dieser Parameter kann dann gegeben sein, oder auch nicht
def test(x = 0):
	print("...")

test()
test(123)

# Warum?
# In Python werden viele Funktionen mit 10, 20, 50, 100 optionalen Parametern definiert
# Wenn ich die Funktion verwende, kann ich nur die Parameter angeben, die ich wirklich brauche

# Beispiel: pandas.read_csv
# pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, skip_blank_lines=True, parse_dates=None, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=<no_default>)
# Diese Funktion hat 40 Parameter
# Über name= kann der Parameter spezifisch angesprochen werden

def demo(pfad, zahl = 0, trennzeichen = ","):
	print("...")

demo("")  # Pfad muss angegeben werden
demo("", zahl=1, trennzeichen=";")
demo("", trennzeichen="-")
demo(pfad="C:\\", trennzeichen=",")

##################################

# Arbitrary Arguments
# Der *-Parameter
# Erlaubt beliebig viele Werte
def summe(*zahlen: int):
	s = 0
	for i in zahlen:  # Innerhalb der Funktion wird dieser Parameter als eine Liste behandelt
		s += i
	print(f"Summe: {s}")

summe()
summe(1)
summe(1, 2)
summe(1, 2, 3, 4, 5)

# Unpacking Operatoren
# Zerlegen eine Liste in ihre Einzelteile
# summe([1, 2, 3])  # Nicht möglich
summe(*[1, 2, 3])  # Nicht möglich

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)
