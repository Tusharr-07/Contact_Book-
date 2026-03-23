contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if len(contacts) == 0:
        print("\nNo contacts found.\n")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']} - {contact['phone']}")
        print()


def search_contact():
    search = input("Enter name or phone to search: ")
    found = False

    for contact in contacts:
        if search.lower() in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print(contact)
            found = True

    if not found:
        print("No contact found.\n")


def update_contact():
    view_contacts()
    if len(contacts) > 0:
        num = int(input("Enter contact number to update: "))
        if 1 <= num <= len(contacts):
            contact = contacts[num - 1]

            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")

            print("Contact updated successfully!\n")
        else:
            print("Invalid number.\n")


def delete_contact():
    view_contacts()
    if len(contacts) > 0:
        num = int(input("Enter contact number to delete: "))
        if 1 <= num <= len(contacts):
            contacts.pop(num - 1)
            print("Contact deleted!\n")
        else:
            print("Invalid number.\n")


# Main Loop
while True:
    print("==== CONTACT BOOK MENU ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        search_contact()

    elif choice == '4':
        update_contact()

    elif choice == '5':
        delete_contact()

    elif choice == '6':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, try again.\n")