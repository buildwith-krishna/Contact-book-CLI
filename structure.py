from storage import load
from storage import save

class ContactBook():
    def save_contact(self):
        name = input("Enter name: ").strip()
        number = input("Enter number: ").strip()
        contacts = load()
        contacts[name] = number
        save(contacts)
        print("<<-Contact Saved->>")

    #Helper function to display saved contacts        
    def show_contacts(self): 
        contacts = load()

        if not contacts:
            print("No contacts found!")
            return
        for name, number in contacts.items():
            print(f"\nName: {name}")
            print(f"Number: {number}\n")

    def delete_contact(self):
        self.show_contacts()
        contacts = load()
        in_contacts = False

        choice = input("Select name: ").strip()
        if choice == "":
            print("Name can't be empty!")
            return 
        for name, number in contacts.items():
            if choice == name:
                in_contacts = True

        if in_contacts == True:
            confirmation = input("Do you want to delete this contact? (y/n) ").lower().strip()
            if confirmation == "y":
                del contacts[name]
                save(contacts)
                print("<<-contact_Deleted->>")
            else:
                return   
        else:
            print("Name does not exist!")
            return


    def update_contact(self):
        self.show_contacts()
        contacts = load()

        contact_name = input("Enter contact's name: ").strip()
        if contact_name == "":
            print("Name can't be empty!")
            return
        in_contact = False

        for name, number in contacts.items():
            if contact_name == name:
                in_contacts = True

        if in_contacts == True:
            new_name = input("Enter new name: ").strip()
            if new_name != "":
                new_number = input("Enter new number: ").strip()
                if new_number != "":
                    contacts[new_name] = new_number
                    save(contacts)
                    print("<<-Contact Updated->>")
                else:
                    print("New number can't be empty!")
                    return
            else:
                print("New name can't be empty!")

        else:
            print("This contact does not exist!")
            return


    def search_contact(self):
        contacts = load()
        find_name = input("Enter name to search: ").strip()
        in_contacts = False
        if find_name == "":
            print("Name can't be empty!")
            return
        for name, number in contacts.items():
            if find_name == name:
                in_contacts = True
                print(f"\nName : {name}")
                print(f"Number : {number}\n")
        if in_contacts == False:
            print("\nThis contact does not exist!\n")

    
