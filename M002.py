# Kommentare
# Text, der nicht ausgeführt wird

# Zwei Varianten: Raute, Docstring

print("Hallo Welt")  # Kommentar in einer Zeile

###################################################

# Variablen
# Werte speichern
# Syntax: <Name> = <Wert>
x = 5
print(x)  # Der Inhalt einer Variable ergibt den Typen der Variable -> x selbst hat keinen Typen

y = "Ich bin ein Text"  # String Variable
print(x, y)  # Mehrere Werte ausgeben

# Datentypen

# Ganze Zahlen: int
x = 2156897302435679_585_230_133_516_782_563_821_568_234_567  # Beliebig Große/kleine Zahlen
print(x)  # _: Tausendertrennzeichen

# Kommazahlen: float
y = 2385697120435468_724.432_867_342958342896  # Kommazeichen: Punkt
print(y)

# Texttypen: str
t1 = "Hallo Welt"  # Doppelte Hochkomma oder einzelne Hochkomma notwendig
t2 = 'Hallo Welt'
print(t1)
print(t2)

# Wahr-/Falschwert: bool
b1 = True
b2 = False
print(b1)

# complex: Komplexe Zahlen
c = 12 + 5j  # i = j

###################################################

# Index
# Aus einer Liste ein/mehrere Elemente entnehmen
text = "Ich bin ein Text"

print(text[0])  # Stelle 0: Das erste Element

print(text[-1])  # Stelle -1: Das letzte Element

print(text[4:6])  # Bereichsindex: Wählt Zeichen von X bis Y (aber ohne Obergrenzen)
print(text[4:7])  # bi -> bin

print(text[-4:])  # Bei einem Bereich kann auch die Ober-/Untergrenze weggelassen werden

###################################################

# Stringfunktionen
# Funktionen auf einen String anwenden
# Wird mit dem Punkt-Operator (.) durchgeführt

# count(Zeichen)
# Zählt, wie oft ein gegebenes Zeichen vorkommt
print(text.count("i"))

# lower(), upper()
# Schreibt den gesamten String lowercase oder UPPERCASE
print(text.lower())
print(text.upper())

print(text)  # Das original bleibt unverändert

# Aufgabe: Alle I's zählen
print(text.lower().count("i"))
print(text.count("I") + text.count("i"))

# len(Variable)
# Gibt die Länge der entsprechenden Variable aus
# Wird für Strings, Listen, Daten, ...
print(len(text))  # Nicht text.len, sondern len(text)

# capitalize(), title()
# Schreibt den ersten/alle Anfangsbuchstaben groß, den Rest klein
print(text.capitalize())
print(text.title())

###################################################

# Arithmetik
z1 = 4
z2 = 7

print(z1 + z2)  # Berechne die Summe, verändere keine Werte

z1 += z2  # Berechne die Summe, und schreibe sie in z1
z1 = z1 + z2  # Längere Form von +=

# Modulo
# Gibt den Rest einer Division zurück
print(9 % 4)  # 1

# Zwei Anwendungsfälle: Gerade/Ungerade prüfen, wie oft kann ich X machen?
print(7 % 2)  # 1 oder 0 (ungerade, gerade)

# Potenz
# X^Y
print(2 ** 3)  # 2 ^ 3 = 8

print(9 ** 0.5)  # Wurzelziehen

print(9 ** -1)  # Bruch umdrehen -> 1/9

# Ganzzahldivision
print(9 / 4)  # 2.25
print(9 // 4)  # 2

# Arithmetik mit Strings
text1 = "Hallo"
text2 = "Welt"

print(text1 + text2)
print(text1 + " " + text2)

text1 += text2

print(text1 * 20)  # Strings multiplizieren