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
  def quit(addressbook):
    nonlocal run
    run = False
  run = True
  while run:
    menu()
    selection = int(input('Enter a selection: '))

    # if selection == 1: 
    #   contacts.show_contacts(addressbook)
    # elif selection == 2:
    #   contacts.add_contact(addressbook)
    # elif selection == 3:
    #   contacts.delete_contact(addressbook)
    # elif selection == 4:
    #   run = False
    # else:
    #   print('\nThat selection is not valid, please try again!\n')

    switch = {
      1: lambda addressbook: contacts.show_contacts(addressbook),
      2: lambda addressbook: contacts.add_contact(addressbook),
      3: lambda addressbook: contacts.delete_contact(addressbook),
      4: quit
    }
    
    if selection in switch:
      switch[selection](addressbook)
    else:
      print('\nThat selection is not valid, please try again!\n')
  
  print('\nGoodbye!\n')


main()
