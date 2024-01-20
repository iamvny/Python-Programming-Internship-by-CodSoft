class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print()

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added: {contact.name}")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            print("Contact Book:")
            for contact in self.contacts:
                contact.display_contact()

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")

            new_contact = Contact(name, phone_number, email)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            contact_book.display_contacts()

        elif choice == "3":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
