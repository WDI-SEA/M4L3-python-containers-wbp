def show_contacts(addressbook):
  print()
  for contact in addressbook:
      print(f"{contact['name']} -- ({contact['email']}) -- {contact['phone']}")
  print()

def add_contact(addressbook):
  name = input('Enter first and last name: ').strip()
  phone = input('Enter phone: ').strip()
  email = input('Enter email: ').strip()

  new_contact = {
      'name': name,
      'phone': phone,
      'email': email
  }
  addressbook.append(new_contact)

  print(f'{name} was added to the address book.')

def delete_contact(addressbook):
  prompt = input('Enter part of the contact name: ').strip()

  index = None
  for i, contact in enumerate(addressbook):
      if prompt in contact['name'].lower():
          index = i

  if index is None:
      print('That contact was not found!')
      return

  deleted_name = addressbook[index]['name']
  del addressbook[index]

  print(f'{deleted_name} was deleted from the address book.')
