'''
You are working for a bank/financial 
institution/credit card company and 
you need to create a chatbot that 
will help new customers 
****choose what kind of account they want**** 
and 
****help get them started signing up.****
'''
#chatbot
#name variable
#age variable
#ask how it can help
#select from a list of options
#one option must end the program

# definition
  
def chatbot():
  print(f'How may I help you, {user_name}?\n')
  print('Option 1: Create a new account')
  print('Option 2: Sign in to an existing account')
  print('Option 3: Get help from a customer service representative')
  print('Option 4: See information on account types')
  print('Option 5: Exits the program.\n')
  try:
    user_help_input = int(input('Please enter a number from 1-5: '))
    if user_help_input == 1:
      create_account(user_age)
      chatbot()
    if user_help_input == 2:
      sign_in()
      chatbot()
    if user_help_input == 3:
      customer_service_representative()
      chatbot()
    if user_help_input == 4:
      information()
      chatbot()
    if user_help_input == 5:
      print('Thank you for using our chatbot! Have a nice day.')
      return False
  except ValueError:
    print('\nThat is not a number from 1-5.\n')
    chatbot()

def create_account(age):
  if age < 18:
    print('\nSorry, but you must be 18 or older to create an account.\n')
  if age >= 18:
    print('What kind of account would you like to create?')
    print('0: Information on account types')
    print('1: Savings account')
    print('2: Checking account')
    print('3: Return to the menu')
    account_type = int(input('Enter 0, 1, 2, or 3: '))
    if account_type == 0:
      information()
      create_account(age)
    if account_type == 1:
      username = input('Please input a username: ')
      password = input('Please input a password: ')
      confirm_password = input('Please confirm your password: ')
      if password != confirm_password:
        print('Sorry, those passwords do not match.')
        password = input('Please input a password: ')
        confirm_password = input('Please confirm your password: ')
    if account_type == 2:
      username = input('Please input a username: ')
      password = input('Please input a password: ')
      confirm_password = input('Please confirm your password: ')
      if password != confirm_password:
        print('Sorry, those passwords do not match.')
        password = input('Please input a password: ')
        confirm_password = input('Please confirm your password: ')
    if account_type == 3:
      pass
def sign_in():
  if user_age < 18:
    print('\nSorry, but you must be 18 or older to own an account.\n')
    return
  print('Please enter your username and password.')
  username = input('Username: ')
  password = input('Password: ')
  print(f'Welcome back, {username}!')
  

def customer_service_representative():
  print('\nConnecting you with a customer service representative.')
  print('Please hold...\n')
  
def information():
  print('\nOur banking system allows for the creation of checking and saving accounts. Checking accounts are for everyday transactional exchanges. Saving accounts are for depositing savings.\n')
# body
program_running = True
print('Welcome to the First Service Bank chatbot.')
user_name = input('What is your name?: ')
user_age = int(input(f'Nice to meet you, {user_name}! What is your age?: '))
while program_running:
  program_running = chatbot()