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

# def delete_contact(addressbook):
#   pattern = input('Enter a part of their name: ').strip().lower()
#   for contact in addressbook:
#     if pattern in contact['name'].lower():
#       addressbook.remove(contact)
#       print(f'{contact["name"]} was deleted.')
#     else:
#       print('Contact Not found!')


def delete_contact(addressbook):
  pattern = input('Enter a part of their name: ').strip().lower()
  idx = None
  for i in range(len(addressbook)):
    if pattern in addressbook[i]['name'].lower():
      idx = i
  
  if idx is None:
    print('Contact Not found!')
    return
  
  deleted_name = addressbook[idx]['name']
  del addressbook[idx]
  print(f'{deleted_name} was deleted.')




