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
  pattern = prompt("Enter a part of their name: ").strip()
  idx = null

  for i in range(0, len(addressbook)):
    if addressbook[i]['name'].index(pattern) >= 0:
      idx = i

  if idx == null:
    print("\nContact not found!\n")
    return

  deleted_name = addressbook[idx]['name']
  addressbook.remove(idx)

  console.log(f"\n{deleted_name} was deleted.")