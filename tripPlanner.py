trip_dict = {
	"Ski trip": {"Tahoe": ["Jess"]},
	"Weekend in Seattle": {"Seattle": ["Katie"]},
	"Yoga in India": {"Mumbai": ["Sahid"]},
	"Trip to Chile": {"Santiago": ["Monica"]}
}
username = ""
'''Get username'''
def get_user():
	username = raw_input("What is your name? ")
	username = username.capitalize()
	return username

'''Be nice and say hello'''
def say_hello():
	print "\nHey " + get_user() + "!"
	print_menu()

'''Show the menu'''
def print_menu():
		print "\n"
		print "*** MENU ***"
		print "(V)iew your friends' trips"
		print "(C)reate a new trip"
		print "(E)xit"                     #Exit doesn't work yet 
		print "\n"
		get_selection()

'''Takes user menu selection, returns string'''
def get_selection():
	while True:
		menu_selection = raw_input("What would you like to do? ")
		menu_selection = menu_selection.upper()
		if menu_selection == "C":
			plan_trip()
		elif menu_selection == "V":
			view_trips()
		elif menu_selection == "E":
			break
		else:
			print "Sorry, I don't understand that option."

'''Shows user all the trips their friends have saved'''
def view_trips():
	print '\n'
	print '# ' + '%-10s | %-10s' % ("CITY","TRIP NAME")
	print '-------------------------'
	number = 1
	for trip_name in trip_dict:
		destination = trip_dict[trip_name].keys()[0]
		friend_list = trip_dict[trip_name][destination]
		print str(number) + ' %-10s | %-10s' % (destination, trip_name)
		number += 1
		for friend in range(len(friend_list)):
			print ' -' + friend_list[friend]
		print '\n'


'''Asks user which city they want to visit, returns name of city'''
def ask_destination():
	destination = raw_input("Which city would you like to go to? ")

	'''This will capitalize the first letter of each word in user input'''
	destination = ' '.join(word[0].upper() + word[1:] for word in destination.split())
	
	return destination

'''Checks destination against trip_dict to see if a friend is already going'''
def trip_exists(destination):
	exists = False
	for i in trip_dict:
		if trip_dict[i].has_key(destination):
			exists = True
	return exists

'''Tells you which friends are going on the trip'''
def friends_going(destination):
	for i in trip_dict:
		if trip_dict[i].has_key(destination):
			friend = trip_dict[i].get(destination)[0]
			return friend

'''Get trip key'''
def get_existing_trip_name(destination):
	for trip in trip_dict:
		if trip_dict[trip].has_key(destination):
			existing_trip_name = trip
			return existing_trip_name

'''Ask user if they want to join their friend'''
def confirm_join_trip(destination):
	friend = friends_going(destination)
	existing_trip_name = get_existing_trip_name(destination)
	print "It looks like " + str(friend) + " wants to go to " + destination + "!"
	wants_to_join = raw_input("Do you want to join? Y/N ")
	if wants_to_join:
		join_trip(destination)
	else:
		create_new(destination)

'''Appends user to their friend's trip'''
def join_trip(destination):
	#username
	existing_trip_name = get_existing_trip_name(destination)
	trip_dict[existing_trip_name][destination].append(username)
	print trip_dict[existing_trip_name][destination]

'''Makes sure trip name isn't taken'''
def trip_name_exists(trip_name):
	for i in trip_dict:
		if trip_dict[i] == trip_name:
			return True
		else:
			return False

'''Lets user name the new trip'''
def name_trip():
	trip_name = raw_input("Give your trip a name: ")
	while trip_name_exists(trip_name):
		print "Sorry, that trip name already exists."
	else:
		return trip_name

'''Create new trip, appends the trip to trip_dict'''
def create_new(destination):
	name_trip()
	trip_dict[trip_name] = {destination: [username]}

'''Lets user plan their trip'''
def plan_trip():
	destination = ask_destination()
	if trip_exists(destination):
		confirm_join_trip(destination)
	else:
		create_new(destination)

######
say_hello()