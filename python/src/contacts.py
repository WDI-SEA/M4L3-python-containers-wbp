def show_contacts(addressbook):
  print()
  for contact in addressbook:
    print(f"{contact['name']} ({contact['email']}): ${contact['phone']}")
  print()

def add_contact(addressbook):
  name = input("Enter name: ").strip()
  phone = input("Enter phone: ").strip()
  email = input("Enter email: ").strip()

  new_contact = {
    "name": name,
    "phone": phone,
    "email": email,
  }

  addressbook.append(new_contact)

  print(f"\n{name} was added.\n")

def delete_contact(addressbook):
  pass
