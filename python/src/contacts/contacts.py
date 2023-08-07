def show_contacts(address_book):
    print("\nContacts:\n")
    for contact in address_book:
        print(f"{contact['name']} {contact['email']} : {contact['phone']}")


def add_contact(address_book):
    new_contact = {}
    print("\nAdding a contact\n")
    for s in ["name", "phone", "email"]:
        new_contact[s] = input(f"Enter {s}: ")
    address_book.append(new_contact)


def delete_contact(address_book):
    print("\nDeleting one or more contacts\n")
    partial = input("Enter a part of their name: ")
    return (
        contact
        for contact in address_book
        if partial.lower() not in contact["name"].lower()
    )
