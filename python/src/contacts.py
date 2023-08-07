def show_contacts(addressbook):
  print()
  for contact in addressbook:
    print(f"{contact['name']} {contact['email']}: {contact['phone']} ")
    print()

def add_contact(addressbook):
  name = input("enter name: ")
  phone = input("enter phone: ")
  email = input("enter email: ")

  new_contact = {
    'name': name,
    'phone': phone,
    'email': email
  }
  addressbook.append(new_contact)

  print(f'\n{name} was added.\n')

def delete_contact(addressbook):
  pattern = input('Enter a part of their name: ').strip()

  # idx = None
  # for i, contact in enumerate(addressbook):
  #   if pattern in contact["name"]:
  #         idx = i

  idx = None
  for i in range(len(addressbook)):
    if pattern in addressbook[i]["name"] and addressbook[i]["name"].index(pattern) >= 0:
        idx = i
          
    if idx == None:
       print("\nContact not found!\n")
       return
    
    deleted_name = addressbook.pop(idx)

    print(f"\n{deleted_name['name']} was deleted.\n")