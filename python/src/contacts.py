def show_contacts(addressbook):
    pass


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

    console.log(f"{new_contact[name]} was added")


def delete_contact(addressbook):
    pass
