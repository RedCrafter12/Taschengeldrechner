konten = []

class Konto:
	def __init__(self,passwort,id):
		self.passwort = passwort
		self.id = id
		self.geld = 10
		
	

while True:
	wahl = input('1.Einloggen 2. Konto erstellen 3.Beenden')
	if wahl == '1':
		nummer = input('Nummer:')
		for k in konten:
			if nummer == k.id:
				passwo = input('Passwort:')
				if passwo == k.passwort:
					while True:
						print(f'Kontostand: {geld}€')
						wahl = input('1.Einzahlen 2.Auszahlen 3.Kontodetails 4.Beeenden -->')
						if wahl == '1':
							geld += int(input('Wie viel? -->'))
						elif wahl == '2':
							geld -= int(input('Wie viel? -->'))
						elif wahl == '3':
							pass
						elif wahl == '4':
							break
	if wahl == '2':
		id = input('Kontonummer=')
		passwort = input('Passwort=')
		neu_konto = Konto(passwort,id)
		konten.append(neu_konto)