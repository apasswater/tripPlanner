
###############################################
'''This is old and shitty code'''
		
'''Check if the city the user typed in is already an existing trip'''
def does_trip_exist(destination):
	extisting_trip = False
	for i in trip_dict:
		if trip_dict[i].has_key(destination):
			friend = trip_dict[i].get(destination)[0]
			existing_trip = True
	if existing_trip == True:
		print "It looks like " + str(friend) + " wants to go to " + destination + "!"
		join_trip()
	else:
		print "It looks like none of your friends have started a trip to " + destination + "." 
		create_new()

'''Asks user where they would like to go'''
def ask_destination():
	while True:
		destination = raw_input('Which city would you like to go to? ')

		'''This will capitalize the first letter of each word in user input'''
		destination = ' '.join(word[0].upper() + word[1:] for word in destination.split())

		confirm = raw_input('You would like to go to ' + destination + '. Is that correct? Y/N: ')
		confirm = confirm.upper()
		if confirm == "Y":
			does_trip_exist(destination)
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
	new_trip = raw_input('Create a new trip? Y/N ')
	new_trip = new_trip.upper()
	if new_trip == 'Y':
		print "Ok, let's get started!"
		### need to create a new trip here ###
	else:
		initial_selection()


'''Present menu, and let user make a selection'''
def initial_selection():
	while True:


		menu_choice = raw_input('What would you like to do? ')
		menu_choice = menu_choice.upper()

		if (menu_choice != "C") and (menu_choice != "V") and (menu_choice != "E"):
			print "Sorry, that's not a valid selection."
		else:
			if menu_choice == "C":
				ask_destination()
			elif menu_choice == "V":
				print trip_dict
			else:
				print "Ok, see you next time!"
			break

initial_selection()
