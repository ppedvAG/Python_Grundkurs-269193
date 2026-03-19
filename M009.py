# input
# Verlangt vom Benutzer eine Eingabe
# Hält den Code auf, bis die Eingabe mit Enter bestätigt wurde

# name = input("Gib deinen Namen ein: ")  # Eingabe
# print(f"Hallo {name}")

# def input(text, default):
# 	eingabe = input("Gib deinen Namen ein: ")
# 	if eingabe == "":
# 		return default
# 	return eingabe

######################################################

# open
# Mit Dateien interagieren
file = open("Log.txt", "w")  # Datei öffnen
file.write("Hallo")  # WICHTIG: Hier wird noch kein Inhalt geschrieben
file.flush()  # Schreibt den Inhalt des Buffers in die Datei
file.close()  # Schreibt den Inhalt des Buffers in die Datei, und schließt den Stream

# WICHTIG: Dateien immer schließen, wenn der Schreib-/Leseprozess abgeschlossen ist

######################################################

# with
# Schließt den Stream am Ende des Blocks automatisch
with open("Log.txt", "r") as readFile:  # Hier wird der Variablenname am Ende definiert
	print(readFile.readline())
# Hier wird das File automatisch geschlossen

######################################################

# Escape-Sequenzen
# Zeichen in einen String einbetten, welche per Tastatur nur schwer/nicht getippt werden können
# https://learn.microsoft.com/de-de/cpp/c-language/escape-sequences?view=msvc-170
text = "Hallo \n Welt"
print(text)

tab = "Hallo \t Welt"
print(tab)

pfad = "C:\\Windows"  # Bei Windows Pfaden werden 2 Backslashes benötigt
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2026_03_18\.venv\Scripts\python.exe"  # Mit rstring können Escape-Sequenzen deaktiviert werden

######################################################

# Pfadoperation
import os.path

projekt = "Python_Grundkurs_2026_03_18"
datei = "Test.py"
x = os.path.join(projekt, datei)  # Pfade betriebssystemagnostisch kombinieren
print(x)

if os.path.exists("Log.txt"):
	print("File existiert bereits")

import sys
print(sys.version)
print(sys.platform)