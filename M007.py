# List Comprehension
# Kurzschreibweise zur Erzeugung von Listen
# Enthält eine Schleife und kann mit einer if-Anweisung versehen werden
zahlen = []
for i in range(0, 100, 2):
	zahlen.append(i)
print(zahlen)

zahlenLC = [i for i in range(0, 100, 2)]  # Schleife Schreiben, links von der Schleife die Schleifenvariable einsetzen (i)
print(zahlenLC)

# if-Anweisung
# -> Filterung

# Beispiel: Nur Primzahlen finden aus einer Range
z = list(range(2, 200))

def isPrime(x):
	# max = int(x / 2)
	if x % 2 == 0:
		return False
	for i in range(3, x - 1):
		if x % i == 0:
			return False  # Keine Primzahl
	return True  # Ist eine Primzahl

primzahlenLC = [i for i in z if isPrime(i)]
print(primzahlenLC)

emails = ["abc@def.de", "abcdef.de"]
emailsLC = [x for x in emails if "@" in x]  # Nur valide Emails filtern
print(emailsLC)

# Linke Seite
# Werte ändern, bevor diese in die LC kommen
f = [3.4, 9.5, 2.2, 5]

fLC = [int(i) for i in f]  # Schneidet alle Kommastellen ab
print(fLC)

eingaben = ["5", "2", "3", "9"]
eingabenLC = [int(i) for i in eingaben]
print(eingabenLC)

# Verschachtelte Schleife
for x in range(10):
	for y in range(10):
		print("...")

einMalEinsLC = [x * y for x in range(10) for y in range(10)]