""" ATM """
import getpass
import string
import os

# creating a lists of users, their PINs and bank statements
users = ['person1', 'person2', 'person3']
pins = ['1234', '5678', '0000']
amounts = [10000, 25000, 30700]
count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users: # user user2 user 3
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('INVALID USERNAME')

# comparing pin
while count < 3:
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	if pin.isdigit():
		if user == 'person1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()

		if user == 'person2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
				
		if user == 'person3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
	else:
		print('PIN CONSISTS OF 4 DIGITS')
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	exit()

print('LOGIN SUCCESFUL, CONTINUE')
print(str.capitalize(users[n]), 'welcome to ATM')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement_(S) \nWithdraw_(W) \nLodgement(L)  \nChange PIN(P)  \nQuit_______(Q) \n: ').lower()
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'EURO ON YOUR ACCOUNT.')
	elif response == 'w':
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		if cash_out%10 != 0:
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES')
		elif cash_out > amounts[n]:
			print('YOU HAVE INSUFFICIENT BALANCE')
		else:
			amounts[n] = amounts[n] - cash_out
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
	elif response == 'l':
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		if cash_in%10 != 0:
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 EURO NOTES')
		else:
			amounts[n] = amounts[n] + cash_in
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
	elif response == 'p':
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			if new_ppin != new_pin:
				print('PIN MISMATCH')
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
	elif response == 'q':
		exit()
	else:
		print('RESPONSE NOT VALID')
