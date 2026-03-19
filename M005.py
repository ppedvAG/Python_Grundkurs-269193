# Schleifen
# Code wiederholen/Code mehrmals ausführen

# while-Schleife
# Enthält eine Bedingung
# Führt den enthaltenen Code solange aus, bis die Bedingung nicht mehr gegeben ist
# Wenn am Ende der Schleife die Bedingung noch gültig ist, beginnt die Schleife von vorne

a = 0
while a < 10:
	print(a)
	a += 1  # Kein ++ in Python
	# Hier wird die Bedingung nochmal ausgewertet, wenn die Bedingung hier noch True ist, geht es von vorne los

print("Nach der Schleife")

# break und continue
# Schleifensteuerung
# break: Bricht die Schleife ab
a = 0
while a < 10:
	print(a)
	a += 1

	if a == 5:
		break  # Beendet hier die Schleife (springt zu Zeile 28)

print("Nach der Schleife")

# continue
# Überspringe allen Code, der nach dem Keyword kommt
# Anwendungsfall: Fehlerbehandlung bei Daten; am Anfang der Schleife
a = 0
while a < 10:
	a += 1
	if a == 5:
		continue  # Überspringt das print, wenn a = 5 ist
	print(a)

print("Nach der Schleife")

# else
# Führt Code nach der Schleife aus, wenn die Schleife nicht mit break beendet wurde
a = 0
while a < 10:
	a += 1
	print(a)
else:
	print("Alles Gut")

# Endlosschleife
while True:
	print("Endlos")

	if a == 100:
		break

###################################################

# for-Schleife
# Schleife, welche immer über eine Collection iterieren muss
# D.h. List, Tuple, Set, Range, Dict, Str, ...

# for-Schleife enthält einen Zeiger, dieser zeigt immer auf ein Element und schreibt dieses in die Laufvariable hinein
# Am Ende der Schleife wird der Zähler um ein Element bewegt (nach rechts)
zahlen = [3, 9, 8, 1, 2, 5]
for i in zahlen:
	print(i)  # i enthält immer den jetztigen Wert

namen = ["Max", "Tim", "Udo"]
for name in namen:
	print(name)  # name enthält immer den jetztigen Namen

# Klassische for-Schleife
# Schleife, die nur einen Zähler hochzählt
for i in range(10):  # int i = 0; i < 10; i++
	print(i)

###################################################

# fstring
# Formatted String
# Code in einen String einbetten
# Sobald der String angelegt wird, wird der Code ausgeführt
zahl = 123
ausgabe = "Die Zahl ist: " + str(zahl)  # Muss hier umgewandelt werden
print(ausgabe)

ausgabeF = f"Die Zahl ist: {zahl}"  # Hier kann in den String jetzt Code eingebaut werden
print(ausgabeF)

teilbarDurch2 = "Die Zahl " + str(zahl) + " ist durch 2 teilbar: " + str(zahl % 2 == 0)
teilbarDurch2F = f"Die Zahl {zahl} ist durch 2 teilbar: {zahl % 2 == 0}"
print(teilbarDurch2)