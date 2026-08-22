def search_contact(contacts):
    search_name = input("Enter the name of the contact you would like to search for: ")
    
    for contact in contacts:
        if contact.lower() == search_name.lower():
            print(f"Contact Name: {contact}, Phone: {contacts[contact]['phone']}, Email: {contacts[contact]['email']}")
            return
        
    print(f"Contact {search_name} not found.")


def add_contact(contacts):
        
    contactName = input("Enter a contact name: ")
    matched_key = None

    for contact in contacts: 
        if contact.lower() == contactName.lower():
            matched_key = contact
            break
    
    if matched_key:
        print(f"Contact {contactName} already exits.") 
        update = input("Would you like to update the contact information? (y/n)")
        if update.lower() == 'y':

            contactPhone = input("Enter a new contact phone number: ")
            contactEmail = input("Enter a new contact email address: ")
            contacts[matched_key] = {"phone": contactPhone, "email": contactEmail}
            print(f"Contact {matched_key} was updated successfully!")
        else: 
            print("Contact was not updated.")
            return
    else:

        contactPhone = input("Enter a contact phone number: ")
        contactEmail = input("Enter a contact email address: ")
        contacts[contactName] = {"phone": contactPhone, "email": contactEmail}
        print(f"Contact {contactName} added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Contact Name: {contact}, Phone: {contacts[contact]['phone']}, Email: {contacts[contact]['email']}") 


def delete_contact(contacts):

    delete_name = input("Enter the name of the contact you would like to delete: ")
    matched_key = None

    for contact in contacts: 
        if contact.lower() == delete_name.lower():
            matched_key = contact
            break

    if matched_key: 
        confirm = input(f"Are you sure you want to delete {matched_key}? (y/n)")
        if confirm.lower() == 'y':
            del contacts[matched_key]
            print(f"Contact {matched_key} was deleted successfully!")
        else:
            print("Contact was not deleted.")
    else:
        print(f"Contact {delete_name} was not found.")
    

contacts = {}

while True:
    print("\n ~~~~~~~~~~~~~~~ Phone Book Menu ~~~~~~~~~~~~~~~ \n")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    if(choice == '1'):
        add_contact(contacts)
    elif(choice == '2'):
        view_contacts(contacts)
    elif(choice == '3'):
        search_contact(contacts)
    elif(choice == '4'):
        delete_contact(contacts) 
    elif(choice == '5'):
        break;
    else:
        print("Invalid choice. Please try again.")
