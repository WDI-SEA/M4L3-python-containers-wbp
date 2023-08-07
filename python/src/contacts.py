def show_contacts(addressbook):
  print('')
  for contact in addressbook:
    print(f"{contact['name']} ({contact['email']}): {contact['phone']}")
  print('')

def add_contact(addressbook):
  name  = input('Enter name: ').strip()
  phone = input('Enter phone: ').strip()
  email = input('Enter email: ').strip()

  newContact = {
    'name': name,
    'phone': phone,
    'email': email
  }

  addressbook.append(newContact)

  print(f'\n{name} was added.\n')

def delete_contact(addressbook):
  pattern = input('Enter a part of their name: ').strip()

  idx = None
  for i in range(len(addressbook)):
    if pattern in addressbook[i]['name']:
      idx = i
      break

  if idx == None:
    print('\nContact Not found!\n');
    return

  deletedName = addressbook[idx]['name']
  addressbook.pop(idx)

  print(f'\n{deletedName} was deleted.\n')
