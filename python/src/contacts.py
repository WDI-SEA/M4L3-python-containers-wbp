def show_contacts(addressbook):
    print(None)
    for contact in addressbook:
        print(f"{contact['name']} ({contact['email']}): {contact['phone']}")
    print(None)


def add_contact(addressbook):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Email: ")

    new_contact = {
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
    }

    addressbook.append(new_contact)

    print(f"\n{new_contact['name']} was added.\n")


def delete_contact(addressbook):
    pattern = input("Enter a part of their name: ").strip()
    idx = None
    for i, contact in enumerate(addressbook):
        if contact["name"].find(pattern) != -1:
            idx = i
            break

    if idx is None:
        print("\nContact Not found!\n")
        return
    deleted_name = addressbook[idx]["name"]
    del addressbook[idx]

    print(f"\n{deleted_name} was deleted.\n")
