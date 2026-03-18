# Bedingungen
# Code, nur unter bestimmten Voraussetzungen ausführen
# if, elif, else

a = 5
b = 8

if a < b:  # Führe den eingerückten Code nur aus, wenn die Bedingung zutrifft
	print("a ist kleiner als b")  # Wenn a 50 ist, wird dieser Code nicht ausgeführt

print("Außerhalb")  # Dieses Statement ist nicht eingerückt, gehört daher nicht zu der Bedingung dazu

if a < b: print("a ist kleiner als b")  # Einzelnes Statement auf der gleichen Zeile

# else
# Sonst
# Wird immer dann ausgeführt, wenn die if-Bedingung nicht zutrifft

if a < b:
	print("...")  # Wenn diese Bedingung ausgeführt wird, kann die else niemals ausgeführt werden
else:  # Bedingungen die durch else automatisch definiert werden: not a < b oder a >= b
	print("a ist größer oder gleich b")  # Kann nur ausgeführt werden, wenn die if-Bedingung nicht zutrifft

# elif
# Sonst, aber mit Bedingung
# Funktioniert wie else, enthält aber einen Sonderfall

if a < b:
	print("...")  # Wenn diese Bedingung ausgeführt wird, kann die elif niemals ausgeführt werden
elif a == 5:
	print("a gleich 5")  # Wenn die if ausgeführt wurde, kann dieser Block niemals ausgeführt werden

#############################################

# Vergleichsoperatoren
# ==, !=       gleich (muss mit 2 gleich-Zeichen definiert werden), ungleich
# <, >		   kleiner, größer
# >=, <=	   größer-gleich, kleiner-gleich

# Logische Operatoren
# and, or, not
# in
if a < b and a == 5:  # & auch erlaubt
	print("Hier sind beide Bedigungen gegeben")

if a < b or a == 5:  # | auch erlaubt
	print("Mindestens eine Bedigung gegeben (eine oder beide)")

if not a < b and not a == 5:  # not: Bedingung umkehren, kann oft gekürzt werden
	print("...")

if a >= b and a != 5:  # Gekürzt
	print("...")

# in
# Prüft, ob ein gegebener Wert in einer Liste enthalten ist (Contains)
zahlen = [1, 2, 3, 4, 5]
if 3 in zahlen:
	print("Die Liste enthält den Wert 3")

if 3 not in zahlen:
	print("Die Liste enthält keine 3")

# Ternary Operator
# Kompaktschreibweise für if/elif/else Blöcke
if a < b:
	print("...")
elif a == 5:
	print("a gleich 5")
else:
	print("...")

# Vorgehensweise: Statement zuerst, danach if, danach else
print("...") if a < b else print("a gleich 5") if a == 5 else print("...")