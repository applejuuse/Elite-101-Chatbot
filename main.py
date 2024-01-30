'''
You are working for a bank/financial 
institution/credit card company and 
you need to create a chatbot that 
will help new customers choose what 
kind of account they want and help 
get them started signing up.
'''
#chatbot
#name variable
#age variable
#ask how it can help
#select from a list of options
#one option must end the program

# definition
def chatbot():
  print('Welcome!')
  user_name = input('What is your name?: ')
  user_age = int(input(f'Nice to meet you, {user_name}! What is your age?: '))
  print('How may I help you?')
  print('Option 1')
  print('Option 2')
  print('Option 3')
  print('Option 4')
  print('Option 5: Exits the program.')
  user_help_input = int(input('Please enter a number from 1-5: '))
  if user_help_input == 1:
    print('Run option 1')
  if user_help_input == 2:
    print('Run option 2')
  if user_help_input == 3:
    print('Run option 3')
  if user_help_input == 4:
    print('Run option 4')
  if user_help_input == 5:
    print('Thank you for using our chatbot! Have a nice day.')
    pass

# body
chatbot()
print('chatbot in a new branch: what a strange oyster')