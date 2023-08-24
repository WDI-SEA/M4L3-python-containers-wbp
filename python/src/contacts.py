def show_contacts(addressbook):
  print()
  for contact in addressbook:
    print(f"{contact['name']} ({contact['email']}): {contact['phone']}");
  print()


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

  print(f"\n{name} was added.\n");

def delete_contact(addressbook):
  pattern = input('Enter a part of their name: ').strip()

  idx = None
  for i in range(len(addressbook)):
    # indexOf() returns -1 if the substring is not found in the string
    if pattern in addressbook[i]['name']:
      idx = i

  if idx == None:
    print('\nContact Not found!\n');
    return
  

  deletedName = addressbook[idx]['name']
  del addressbook[idx]

  print(f"\n{deletedName} was deleted.\n")


