# List
# Sammlung von Elementen
# Kann beliebig viele/beliebige Typen enthalten
meineListe = []  # Leere Liste
meineListe = list()  # Leere Liste

meineListe = [1, 2, 3, 4]  # Liste mit Initialwerten
print(meineListe)  # Liste kann einfach in der Konsole ausgegeben werden

# Index
print(meineListe[0])

print(meineListe[-1])

print(meineListe[1:3])  # In der Konsole eckige Klammern -> List

# append(Element)
# Fügt ein neues Element hinzu
meineListe.append(5)
print(meineListe)

# remove(Element), pop(Index)
# remove: Sucht das Element, und entfernt das erste Vorkommen
# pop: Entfernt das Element am gegebenen Index
meineListe.append(3)
print(meineListe)
meineListe.remove(3)  # Suche 3, lösche erstes Vorkommen
print(meineListe)

meineListe.pop(0)  # Lösche die erste Zahl (Index 0)
print(meineListe)

# sort()
# Sortiert die Liste
meineListe.sort()
print(meineListe)

meineListe.sort(reverse=True)  # Absteigend Sortieren
print(meineListe)

# extend(Andere Liste)
# Zwei Listen verknüpfen
l2 = [1, 2, 3]
meineListe.append(l2)  # Selten sollten hier ganze Listen angehängt werden
print(meineListe)  # Achtung: Verschachtelte Liste

meineListe.remove(l2)
meineListe.extend(l2)  # Eindimensional, wie geplant
print(meineListe)

# Alternative: +=
meineListe += l2  # Selbes Ergebnis wie extend
print(meineListe)

#######################################

# Tupel
# Wie eine Liste, kann aber nicht verändert werden
# Verwendung: Werte, an andere Entwickler weitergeben
tupel = ("Hallo", "Welt")
print(tupel[0])
print(tupel[-1])

#######################################

# range
# Bereich von X bis Y
r = range(0, 10)  # Hier auch Obergrenze exkludiert
print(r)  # Hier wird nur der Generator selbst ausgegeben -> ausführen um Zahlen zu erhalten

print(list(r))  # Generator ausführen über eine Konvertierung zur Liste

r2 = range(0, 100, 10)  # Schrittgröße mitangeben (10-er Abstände)
print(list(r2))

#######################################

# set
# Liste, die aber keine Duplikate erlaubt
s = {1, 2, 3}
print(s)  # Kann in der Konsole über { } erkannt werden

s.add(1)  # Element hinzufügen, sagt nichts, wenn das Element schon existiert
print(s)

# Anwendungsfall: Deduplizieren
zahlen = [1, 2, 2, 3, 4, 4, 4, 5]
zahlen = set(zahlen)  # Konvertieren, hier werden Duplikate entfernt
zahlen = list(zahlen)  # Zurückkonvertieren zur Liste
print(zahlen)

#######################################

# dict
# Set, bei dem jeder Inhalt einen Schlüssel (Namen) hat
person = ["Max", "Mustermann", 33, "Zuhause"]  # Diese Liste hat keine Beschreibungen (ungünstig)

personDict = {
	"Vorname": person[0],
	"Nachname": "Mustermann",
	"Alter": 33,
	"Adresse": "Zuhause"
}

print(person[2])  # Hier nicht klar, was [2] beinhält
print(personDict["Alter"])  # Hier ist sofort klar, was hier enthalten ist

personDict["Geschlecht"] = "M"  # Neue Daten eintragen
print(personDict)

personDict.get("Hallo")  # Sicher
# personDict["Hallo"]  # Nicht sicher

print(personDict.keys())
print(personDict.values())
print(personDict.items())

#######################################

# Konvertierung
# Umwandlung von Daten in andere Typen
f = 328597.12587
i = int(f)  # Kommastellen abschneiden
print(i)

ergebnis = 28
ergebnis = str(ergebnis)  # Wandle das Ergebnis zu einem String um
print("Das Ergebnis ist: " + ergebnis)

eingabe = "123"
print(int(eingabe))  # string zu int umwandeln (z.B. Usereingabe)
print(eingabe * 2)  # 123123 (?)
print(int(eingabe) * 2)  # 246