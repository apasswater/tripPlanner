trip_dict = {
	"Tahoe":"Jess"
}
print "Welcome to tripPlanner!"
username = raw_input('What is your name? ')
username = username.capitalize()

'''Loop indefinitely until user confirm is yes'''
while True:
	destination = raw_input('Hey ' + username + '! Where would you like to go? ')

	'''This will capitalize the first letter of each word in user input'''
	destination = ' '.join(word[0].upper() + word[1:] for word in destination.split())

	confirm = raw_input('You would like to go to ' + destination + '. Is that correct? Y/N: ')
	confirm = confirm.upper()
	if confirm == "Y":
		break
	else:
		print "My bad. Let's try this again. "

'''Function for user joining a trip'''
def join_trip():
	join_confirm = raw_input('Do you want to join? Y/N ')
	join_confirm = join_confirm.upper()
	if join_confirm == 'Y':
		print "Great, I've added you to the trip."
	else:
		create_new()

'''Function to create a new trip'''
def create_new():
	new_trip = raw_input('Create a new trip? ')
	new_trip = new_trip.upper()
	if new_trip == 'Y':
		print "Ok, let's get started!"
	else:
		print "Ok, come back any time to check other trips!"

# Check to see if the trip already exists
# User can either join an existing trip or create a new one
def does_trip_exist():
	if trip_dict.has_key(destination):
		friend = trip_dict.get(destination)
		print "It looks like " + friend + " wants to go to " + destination + "!"
		join_trip()
	else:
		print "It looks like none of your friends have started a trip to " + destination + "." 
		create_new()

does_trip_exist()