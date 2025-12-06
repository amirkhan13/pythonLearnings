import sys

contacts = []


def add_Contact():
    indv_contact = {}

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = int(input("Enter your contact number: "))

    indv_contact["name"] = name
    indv_contact["email"] = email
    indv_contact["phone"] = phone

    contacts.append(indv_contact)
    print("Contact Added Successfully!!")


def update_Contact():
    name = input("Enter the name of the contact you want to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("What do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Phone number")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                new_name = input("Enter new name: ")
                contact["name"] = new_name
                print("Name updated successfully!")

            elif choice == "2":
                new_email = input("Enter new email: ")
                contact["email"] = new_email
                print("Email updated successfully!")

            elif choice == "3":
                new_phone = int(input("Enter new phone number: "))
                contact["phone"] = new_phone
                print("Phone number updated successfully!")

            else:
                print("Invalid choice")

            return

    print("Contact not found!")


def read_Contact():
    if len(contacts) == 0:
        print("No contacts available to search!")
        return

    print("How do you want to search the contacts?")
    print("1. By name")
    print("2. By phone")

    choice = input("Enter your choice (1/2): ")

    # Search by name
    if choice == "1":
        name = input("Enter the name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("Contact found!")
                print(f"Name: {contact['name']}")
                print(f"Email: {contact['email']}")
                print(f"Phone: {contact['phone']}")
                found = True
                break

        if not found:
            print("No contact found with this name.")

    # Search by phone
    elif choice == "2":
        phone = int(input("Enter phone number to search: "))
        found = False

        for contact in contacts:
            if contact["phone"] == phone:
                print("Contact found!")
                print(f"Name: {contact['name']}")
                print(f"Email: {contact['email']}")
                print(f"Phone: {contact['phone']}")
                found = True
                break

        if not found:
            print("No contact found with this phone number.")

    else:
        print("Invalid choice!")


def delete_Contact():

    if len(contacts) == 0:
        print("No contacts to delete!")
        return

    phone = int(input("Enter phone number to delete the contact: "))

    found = False

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break

    if not found:
        print("No contact found with the given number!")

while True:
    print("\nWhat action do you want to perform?")
    print("1. Add contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_Contact()
    elif choice == "2":
        read_Contact()
    elif choice == "3":
        update_Contact()
    elif choice == "4":
        delete_Contact()
    elif choice == "5":
        sys.exit()
    else:
        print("Invalid Choice!")
