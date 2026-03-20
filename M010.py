# Klassen
# Bauplan/Struktur für Daten
# Klasse wird später in Form von Objekten instanziert
# Die Klasse selbst enthält keine konkreten Daten, sondern nur Behälter/Definitionen für diese Daten
# Die Objekte bekommen dann konkrete Daten

# Datentypen
# - int: Ganze Zahl
# - float: Kommazahl
# - str: Text
# - list: Sammlung von Elementen
# - Person: ? (nicht einfach beschreibbar -> Klasse)

class Person:  # Klammern optional, werden für Vererbung verwendet
	"""
	docstring

	Klassen/Funktionen beschreiben

	Mit Mauscursor auf den Typnamen bewegen -> Text lesen
	"""
	def __init__(self, vorname: str, nachname: str, alter: int, geschlecht: str):
		"""
		__init__

		Code, der bei Objekterstellung ausgeführt wird

		Hier werden die Felder, die die Klasse besitzen soll, gesetzt

		Person: Vorname, Nachname, Alter, Geschlecht, ...
		"""
		self.vorname = vorname  # Über diese Anweisung wird der Person-Klasse ein Feld gegeben
		self.nachname = nachname  # Über einen Parameter (in der Klammer bei __init__) müssen hier Objekterstellung Daten mitgegeben werden
		self.alter = alter
		self.geschlecht = geschlecht

	def __str__(self):
		return f"{self.vorname}, {self.nachname}, {self.alter}, {self.geschlecht}"


# Objekte
# Konkrete Instanzen von der Klasse
# Haben alle Felder/Funktionen von der Klasse
# Hier werden die konkreten Daten hineingeschrieben
p1 = Person("Max", "Mustermann", 23, "M")  # Objekt erstellen mit <Name>()
p2 = Person("Max", "Muster", 43, "D")  # Objekt erstellen mit <Name>()
# Hier können jetzt beliebig viele Objekte erzeugt werden

print(p1.vorname)  # Daten aus den Objekten wieder herausgreifen

##########################################

# Datenklasse und Funktionsklasse
# Datenklasse: Behälter für Daten (hier Person)
# Funktionsklasse: Klasse, die Dinge tut (z.B. TextIOWrapper für Dateiinteraktion)
class Rechner:
	"""
	Diese Klasse hat Funktionen (mit def), hält aber keine Daten
	"""
	def add(self, x, y):
		return x + y

	def sub(self, x, y):
		return x - y

r = Rechner()
r.add(3, 4)

##########################################

print(p1.__str__())  # <__main__.Person object at 0x0000029C4D2AD010>
print(p1.__str__())  # Max, Mustermann, 23, M