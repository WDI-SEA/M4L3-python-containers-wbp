def show_contacts(addressbook):
  for contact in addressbook:
    print(f'{contact["name"]} ({contact["email"]}): {contact["phone"]}')

def add_contact(addressbook):
  name  = input('Enter name: ').strip()
  phone = input('Enter phone: ').strip()
  email = input('Enter email: ').strip()
  newContact = {
    'name': name,
    'phone': phone,
    'email': email
  };
  addressbook.append(newContact)
  print(f'{name} was added.')

def delete_contact(addressbook):
  pattern = input('Enter a part of their name: ').strip().lower()
  for contact in addressbook:
    if pattern in contact['name'].lower():
      addressbook.remove(contact)
      print(f'{contact["name"]} was deleted.')
    else:
      print('Contact Not found!')


  # #   if pattern in contact['name'].lower():
  # #     addressbook.remove(contact)
  # #     print(f'{contact["name"]} was deleted.')
  #   if pattern not in contact['name'].lower():
  #     print('Contact Not found!')
  #   else:
  #     addressbook.remove(contact)
  #     print(f'{contact["name"]} was deleted.')






