from peewee import *
def main():
	menu()
#database
db = SqliteDatabase('jugglers.sqlite')

#Create model class
class Juggler(Model):
	name = CharField()
	country = CharField()
	catches = IntegerField()

	#link this model to DB
	class Meta:
		database = db

	def __str__(self):
		return f'{self.name} is from {self.country} and has {self.catches} catches'

#connect to DB, create tables
db.connect()
db.create_tables([Juggler])



#Menu Add, Search By Name, update catches, delete
#found on YouTube tutorial - Python Programming creating a Menu
def menu():
	print('Please select an option')
	print('1. Add Juggler')
	print('2. Search By Name')
	print('3. Update Catches')
	print('4. Delete Juglgers')
	choice = int(input('Enter Coice: '))

	if choice == 1:
		addJuggler()
	elif choice == 2:
		searchByName()
	elif choice == 3:
		updateCatches()
	elif choice == 4:
		deleteJuggler()
	else:
		print('Invalid selection')
		menu()
#add
#Name, Country, Catches
def addJuggler():
	name = input('What is the jugglers name? ')
	country = input('What country are they from? ')
	catches = input('How many catches? ')

	nameEntry = Juggler(name = name, country = country, catches = catches)
	nameEntry.save()
	menu()
#search by name
def searchByName():
	nameInput = input('What is the name of the juggler you are looking for? ')
	query = Juggler.get(Juggler.name == nameInput)
	print(query)
	menu()

#update catches
def updateCatches():
	name = input('Name of the juggler you want to update catches: ')
	updatedCatches = input('How many catches did they make? ')

	updateQuery = Juggler.update(Juggler.catches == updatedCatches).where(Juggler.name == name)

	updateQuery.execute()
	getJugger = Juggler.get(Juggler.name == name)
	print(getJugger)
	menu()
#delete 
def deleteJuggler():
	name = input('Which juggler do you want to delete? ')
	deleteQuerry = (Juggler.delete().where(Juggler.name == name))
	deleteQuerry.execute()
	Juggler.save()
	print(name, 'was deleted from the database')
	menu()

main()