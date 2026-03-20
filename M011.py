# Datenbank
# Benötigt einen Datenbanktreiber (je nach Datenbanksystem)
# MSSQL: pyodbc

import pyodbc

connString = "Driver={ODBC Driver 17 for SQL Server},Server=WIN11-LK3,Database=Northwind,Trusted_Connection=yes,"
with pyodbc.connect(connString) as conn:  # Verbindung herstellen
	cursor = conn.cursor()  # Cursor holen, wird für SQL-Statements verwendet
	data = cursor.execute("SELECT * FROM Customers").fetchall()  # Daten laden anhand von einem SELECT

	# Model Klasse
	# Automatisch: sqlAlchemy
	class Customer:
		def __init__(self, CustomerID, CompanyName, ContactName):
			self.customerID = CustomerID
			self.companyName = CompanyName,
			self.contactName = ContactName
			print("...")

	customers = []
	for row in data:
		c = Customer(row[0], row[1], row[2])
		customers.append(c)

	for customer in customers:
		print(customer.customerID)  # Anstatt customer[0]