import contacts.contacts

address_book = [
    {"name": "Bruce Wayne", "phone": "555-123-4567", "email": "bruce@wayne.com"},
    {"name": "Clark Kent", "phone": "555-222-3333", "email": "clark@dailyplanet.com"},
    {"name": "Diana Prince", "phone": "555-444-5555", "email": "diana@amazon.com"},
]
menus = [
    "[1] Display all contacts",
    "[2] Add a new contact",
    "[3] Delete a contact",
    "[4] Exit",
]


def main(address_book):
    selection = ""
    while selection != "4":
        for menu in menus:
            print(menu)
        selection = input("Enter a selection: ")
        match selection:
            case "1":
                contacts.contacts.show_contacts(address_book)
            case "2":
                contacts.contacts.add_contact(address_book)
            case "3":
                address_book = contacts.contacts.delete_contact(address_book)
            case "4":
                print("Goodbye!")
            case _:
                print("That selection is not valid, please try again!")
        print("")


main(address_book)
