# Ü003

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