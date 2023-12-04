import contacts

def menu():
  print('[1] Display all contacts');
  print('[2] Add a new contact');
  print('[3] Delete a contact');
  print('[4] Exit');

def main():
  
  addressbook = [
    {
      'name': 'Bruce Wayne',
      'email': 'bruce@wayne.com', 
      'phone': '555-123-4567'
    }, {
      'name': 'Clark Kent',
      'email': 'clark@dailyplanet.com', 
      'phone': '555-222-3333'
    }, {
      'name': 'Diana Prince',
      'email': 'diana@amazon.com', 
      'phone': '555-444-5555'
      }
  ]

  run = True
  
  while run:
    menu()
    selection = int(input('Enter a selection: '))

    if selection == 1:
        contacts.show_contacts(addressbook)
    elif selection == 2:
        contacts.add_contact(addressbook)
    elif selection == 3:
        contacts.delete_contact(addressbook)
    elif selection == 4:
        run = False
        print('\nGoodbye!\n')
    else:
        print('\nThat selection is not valid, please try again!\n')

main()