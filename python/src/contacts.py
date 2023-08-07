def show_contacts(addressbook):
  print();
  for contact in addressbook:
    print(f'{contact.name} ({contact.email}): {contact.phone}');
  print();

def add_contact(addressbook):
  name = input('Enter name: ').strip();
  phone = input('Enter phone: ').strip();
  email = input('Enter email: ').strip();
 
  newContact = {
    name: name,
    phone: phone,
    email: email,
  }
  addressbook.push(newContact);

  print(f'\n{name} was added.\n')

def delete_contact(addressbook):
  pattern = input('Enter a part of their name: ').strip();

  idx = None;
  for i in addressbook.len():
    if (addressbook[i]['name'].list.index(pattern)>=0):
      idx =i;

  if (idx ==None):
    print('\nContact Not Found\n')
    return;

  deletedName = addressbook[idx]['name'];
  addressbook.pop(idx,1);

  print(f'\n {deletedName} was deleted.\n')