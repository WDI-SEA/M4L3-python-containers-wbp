def show_contacts(addressbook):
  print()
  for contact in addressbook:
    print(f"{contact['name']} ({contact['email']}): {contact['phone']}")
  print()

def add_contact(addressbook):
  name = input("Enter Name: ").strip()
  phone = input("Enter phone: ").strip()
  email = input("Enter email: ").strip()

  new_contact = {
    "name": name,
    "phone": phone,
    "email": email
  }

  addressbook.append(new_contact)

  print(f"{name} was added.")

def delete_contact(addressbook):
  pattern = input("Enter a part of their name: ").strip()

  for i, contact in enumerate(addressbook):
    # check each contact if it contains the substring
    if pattern in contact["name"]:
      deleted_name = contact["name"]
      addressbook.pop(i)
      print(f"{deleted_name} was deleted")

    return
  # if we reach the end of the iteration, we have not found a match
  print("Contact not found!")
