# Ü004

# Ü1
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]

if len(list1) > len(list2) and len(list1) > len(list3):
	print("list1 ist die längste")
if len(list2) > len(list1) and len(list2) > len(list3):
	print("list2 ist die längste")
if len(list3) > len(list1) and len(list3) > len(list2):
	print("list3 ist die längste")

# Alternative
laengen = [len(list1), len(list2), len(list3)]
hoechste = max(laengen)  # laengen.sort() -> laengen[-1]

if len(list1) == hoechste:
	print("list1 ist die längste")
if len(list2) == hoechste:
	print("list2 ist die längste")
if len(list3) == hoechste:
	print("list3 ist die längste")

# Ü2
list4 = list1 + list2 + list3
if 3 in list4 or 7 in list4 or 10 in list4:
	print("...")

gesucht = {3, 7, 10}
print(gesucht.intersection(list4))

print(gesucht.intersection(list1))
print(gesucht.intersection(list2))
print(gesucht.intersection(list3))

##################################################

# Ü005

# Ü1

# i = 0
# while i < 100:
# 	i += 1

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# Ü2
for i in range(1, 201):
	letzteZiffer = i % 10
	letztenBeidenZiffern = i % 100

	letzteZifferStr = str(i)[-1]
	letztenBeidenZifferStr = str(i)[-2:]

	if letztenBeidenZiffern in [11, 12, 13]:
		print(f"{i}th")
	elif letzteZiffer == 1:
		print(f"{i}st")
	elif letzteZifferStr == "2":  # Sonderfall: String konvertieren
		print(f"{i}nd")
	elif letzteZiffer == 3:
		print(f"{i}rd")
	else:
		print(f"{i}th")

# Ü3
import time
for i in range(3600):
	min = i // 60  # 150 sek / 60 = 2.5 -> 2
	sek = i % 60  # 150 sek % 60 = 30
	print(f"{min}:{sek}")
	# time.sleep(1)

for m in range(60):
	for s in range(60):
		print(f"{m}:{s}")
		# time.sleep(1)

# Ü4
for m in range(1, 11):
	for s in range(1, 11):
		print(f"{m} x {s} = {m * s}")

##################################################

# M006

# Ü1
def maximum(*zahlen):
	l = list(zahlen)
	l.sort()
	print(l[-1])

def maximum(*zahlen):
	x = zahlen[0]  # Bonus-Lösung
	for i in zahlen:
		if i > x:
			x = i
	print(x)

# Ü2
def countCase(text: str):
	k = 0
	g = 0
	s = 0
	for zeichen in text:
		if zeichen.islower():
			k += 1
		elif zeichen.isupper():
			g += 1
		else:
			s += 1
	print(f"Kleinbuchstaben: {k}, Großbuchstaben: {g}, Sonderzeichen: {s}")

countCase("Hallo Welt")

# Ü3
def printTeilnehmer(*tn):
	gesamt = ""
	if len(tn) == 0:
		gesamt = "Keine Teilnehmer"
	elif len(tn) == 1:
		gesamt = tn[0]
	else:
		for t in tn[0:-1]:
			gesamt += t
			gesamt += ", "
		gesamt = gesamt.strip(", ")  # Muss wieder in die Variable zurückgeschrieben werden
		gesamt += " und " + tn[-1]
	print(gesamt)

printTeilnehmer()
printTeilnehmer("Max")
printTeilnehmer("Max", "Tim", "Udo")

##################################################

# M007

# Ü1
print([i + 12 for i in range(1, 31) if i % 6 == 0])

# Ü2
text = "Ich bin ein Text"
print([zeichen.upper() for zeichen in text if zeichen.islower()])

# Ü3
split = text.split(" ")
print(split)

print([wort[0].upper() for wort in split])

# Ü4
print([wort for wort in split if len(wort) <= 3])

##################################################

# M008

# Ü2
while True:
	zahl1 = input("Gib eine Zahl ein: ")
	zahl2 = input("Gib eine weitere Zahl ein: ")
	if not zahl1.isnumeric() or not zahl2.isnumeric():
		exit()

	zahl1 = int(zahl1)
	zahl2 = int(zahl2)

	while True:
		operation = input("1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division")
		if operation.isnumeric():
			operationInt = int(operation)
			if operationInt in [1, 2, 3, 4]:
				break  # Wenn die Schleife einfach ausläuft (kein break), geht sie wieder von vorne los

	if operationInt == 1:
		print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
	elif operationInt == 2:
		print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
	elif operationInt == 3:
		print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
	elif operationInt == 4:
		print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")

	frage = input("Wiederholen? (Y)")
	if frage != "Y":
		break
