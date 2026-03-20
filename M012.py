# Fehlerbehandlung
# Abstürze verhindern, die nicht mit einer if-Anweisung verhindert werden können
# Beispiel: Verbindungsaufbau Datenbank (muss versucht werden, kann im Vorheinein nicht vorgesagt werden)

# Simples Beispiel mit if
eingabe = input("Gib eine Zahl ein: ")
if eingabe.isnumeric():
	zahl = int(eingabe)

# Try-Except
# Abstürze verhindern
try:
	eingabe = input("Gib eine Zahl ein: ")
	zahl = int(eingabe)  # Ohne try-except stürzt hier das Skript ab
except ValueError:  # Wenn ein ValueError auftritt, wird dieser Block ausgeführt
	print("Eingabe ist keine Zahl")
except EOFError:  # Programmabbruch mit Strg + D
	print("Programm sollte abgebrochen werden")
except:  # Generische Klausel, wird bei allen ANDEREN Fehlern ausgeführt
	print("Anderer Fehler")  # Bei ValueError oder EOFError wird dieser Block nicht ausgeführt
else:  # Wenn der Try-Block vollständig und fehlerfrei durchläuft, wird else ausgeführt
	print("Im try-Block keine Fehler")
finally:  # Wird immer ausgeführt
	print("Immer")

# Skript läuft normal weiter
print("Nach der Konvertierung")

#################################################

# raise
# Skript abstürzen lassen
# Warum?
# Weil der User von dem Code, der abstürzen kann, selbst entscheiden soll, wie der Fehler abgehandelt werden soll
# Mit try-except kann der Absturz verhindert werden, und eigener Code für den Fehler definiert werden
# z.B. Datenbankverbindung

# Der User kann mit try-except frei entscheiden, wo der Fehler angezeigt (Konsole, GUI, Datenbank, Webseite, Log, ...)
try:
	raise OverflowError("Hallo")  # Hier wird nur die Fehlermeldung definiert
except OverflowError as e:  # Bei except kann mit as <Name> auf den Fehler zugegriffen werden
	print(e)  # Hier kann der User frei entscheiden, was mit der Fehlermeldung passiert

# Traceback
# Log, das im Code einen Hinweis gibt, wo der Fehler aufgetreten ist
try:
	raise OverflowError("Hallo")
except OverflowError as e:
	import traceback
	ex = traceback.format_exception(e)  # Exception zu einer Liste konvertieren
	print(ex)