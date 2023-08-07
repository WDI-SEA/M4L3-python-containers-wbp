import contacts

addressbook = []

def menu():
  print('[1] Display all contacts')
  print('[2] Add a new contact')
  print('[3] Delete a contact')
  print('[4] Exit')

def main():
  run = True
  # def quit(addressbook):
  #   nonlocal run
  #   run = False

  while run:
    selection = input("Enter a selection: ").strip()

    match selection:
      case "1":
        contacts.show_contacts(addressbook)
      case "2":
        contacts.add_contact(addressbook)
      case "3":
        contacts.delete_contact(addressbook)
      case "4":
        run = False
      case _:
        print("\nThat selection is not valid, please try again!\n")


    # switch = {
    #   "1": lambda addressbook : contacts.show_contacts(addressbook),
    #   "2": lambda addressbook : contacts.add_contact(addressbook),
    #   "3": lambda addressbook : contacts.delete_contact(addressbook),
    #   "4": quit
    # }

    # # defualt case
    # if selection in switch:
    #   switch[selection](addressbook)
    # else:
    #   print("\nThat selection is not valid, please try again!\n")

main()

# my_function = lambda x, y: x + y