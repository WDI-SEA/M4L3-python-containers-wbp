import contacts

addressbook = [
  { 'name': 'Bruce Wayne', 'phone': '555-123-4567', 'email': 'bruce@wayne.com' },
  { 'name': 'Clark Kent', 'phone': '555-222-3333', 'email': 'clark@dailyplanet.com' },
  { 'name': 'Diana Prince', 'phone': '555-444-5555', 'email': 'diana@amazon.com' }
]

def menu():
  print('[1] Display all contacts')
  print('[2] Add a new contact')
  print('[3] Delete a contact')
  print('[4] Exit')

def main():
  run = True
  while run:
    menu()
    selection = int(input('Enter a selection: '))
    if selection == 1:
      # print('\nYou have selected option 1\n')
      contacts.show_contacts(addressbook)
      break
    elif selection == 2:
      # print('\nYou have selected option 2\n')
      contacts.add_contact(addressbook)
      break
    elif selection == 3:
      # print('\nYou have selected option 3\n')
      contacts.delete_contact(addressbook)
      break
    elif selection == 4:
      run = False
      break
    else:
      print('\nThat selection is not valid, please try again!\n')

  print('\nGoodbye!\n')

main()
