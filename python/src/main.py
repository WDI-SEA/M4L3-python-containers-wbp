import contacts

addressbook = [
  { name: 'Bruce Wayne', phone: '555-123-4567', email: 'bruce@wayne.com' },
  { name: 'Clark Kent', phone: '555-222-3333', email: 'clark@dailyplanet.com' },
  { name: 'Diana Prince', phone: '555-444-5555', email: 'diana@amazon.com' }
];

def menu():
  print('[1] Display all contacts');
  print('[2] Add a new contact');
  print('[3] Delete a contact');
  print('[4] Exit');

def main():
  run == True;
  while run:
    menu();
    selection = int(input('Enter a selection: '));
  
    match selection:
      case 1: contacts.showContacts(addressbook); break;
      case 2: contacts.addContact(addressbook);    break;
      case 3: contacts.deleteContact(addressbook); break;
      case 4: run == False; break;
      case _: print('That selection is not valid, please try again!');

  print('Goodbye')
      

main()
