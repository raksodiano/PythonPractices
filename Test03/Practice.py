# Contact list
import json
import uuid


def menu():
    print("\nContacts List:")
    print("1. List")
    print("2. Add")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")


def list_contacts():
    try:
        with open('Contacts.json', 'r') as file:
            contacts = json.load(file)

        if not contacts:
            print("No contacts to display.")
        else:
            for index, contact in enumerate(contacts, start=1):
                print(
                    f"\nContact #{index} "
                    f"\nName: {contact['name']} "
                )

    except FileNotFoundError:
        with open('Contacts.json', 'w') as file:
            json.dump([], file)
        print("No contacts to display.")

    except json.JSONDecodeError:
        print("The file 'Contacts.json' is empty or contains invalid format.")


def add_contact():
    contact = {}

    try:
        with open('Contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

    contact['id'] = str(uuid.uuid4())
    contact['name'] = input("Enter the full name of the contact: ")
    contact['phone'] = input("Enter the contact's phone number: ")
    contact['email'] = input("Enter the contact's email address: ")
    contact['direction'] = input("Enter the contact's address: ")

    contacts.append(contact)

    with open('Contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

    print(f"Contact {contact['name']} has been successfully added")


def search_contact():
    number = input("Enter the number of the contact you wish to see in detail: ")

    if number.isdigit():
        number = int(number) - 1

        try:
            with open('Contacts.json', 'r') as file:
                contacts = json.load(file)

            if 0 <= number < len(contacts):
                contact = contacts.pop(number)

                print(
                    f"\nName: {contact['name']} "
                    f"\nPhone: {contact['phone']} "
                    f"\nEmail: {contact['email']} "
                    f"\nDirection: {contact['direction']}"
                )

            else:
                print("Index out of range. No contact to remove.")

        except FileNotFoundError:
            print("The file 'Contacts.json' does not exist.")
        except json.JSONDecodeError:
            print("The file 'Contacts.json' contains invalid JSON or is empty.")
    else:
        print("Please, enter a valid number")


def delete_contact():
    number = input("Enter the contact number you wish to delete: ")

    if number.isdigit():
        number = int(number) - 1

        try:
            with open('Contacts.json', 'r') as file:
                contacts = json.load(file)

            if 0 <= number < len(contacts):
                removed_contact = contacts.pop(number)

                with open('Contacts.json', 'w') as file:
                    json.dump(contacts, file, indent=4)

                print(f"Contact at number {number} has been removed: {removed_contact['name']}")
            else:
                print("Index out of range. No contact to remove.")

        except FileNotFoundError:
            print("The file 'Contacts.json' does not exist.")
        except json.JSONDecodeError:
            print("The file 'Contacts.json' contains invalid JSON or is empty.")

    else:
        print("Please, enter a valid number")


def contact_list():
    while True:
        menu()
        option = input("Select an option: ")

        if option == "1":
            list_contacts()
        elif option == "2":
            add_contact()
        elif option == "3":
            search_contact()
        elif option == "4":
            delete_contact()
        elif option == "5":
            print("Leaving")
            break


contact_list()
