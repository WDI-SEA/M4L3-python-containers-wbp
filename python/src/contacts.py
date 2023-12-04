def show_contacts(addressbook):
  for contact in addressbook:
    print('')
    print(f"{contact['name']} ({contact['email']}): {contact['phone']}")
    print('')

def add_contact(addressbook):
  name  = str(input('Enter name: ')).strip()
  phone = str(input('Enter phone: ')).strip()
  email = str(input('Enter email: ')).strip()

  new_contact = {
    'name': name,
    'phone': phone, 
    'email': email
  }
  addressbook.append(new_contact)

  print(f"\n{new_contact['name']} was added.\n")

def delete_contact(addressbook):
  pattern = str(input('Enter a part of their name: ')).strip()

  idx = ''
  for i in range(len(addressbook)):
    if pattern in addressbook[i]['name']:
      idx = int(i)
  
  if idx == '':
    print("\nContact Not Found!\n")
    return
  
  deleted_name = addressbook[idx]['name']
  del addressbook[idx]

  print(f"\n{deleted_name} was deleted from address book list position {idx}.\n")
    
