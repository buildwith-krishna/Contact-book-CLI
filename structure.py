from storage import load
from storage import save

class ContactBook():
    def save_contact(self):
        name = input("Enter name: ").strip()
        number = input("Enter number: ").strip()
        data = load()
        data[name] = number
        save(data)
        print("<<-Contact Saved->>")

    #Helper function to display saved contacts        
    def show_contacts(self): 
        data = load()

        if not data:
            print("No contacts found!")
            return
        for name, number in data.items():
            print(f"\nName: {name}")
            print(f"Number: {number}\n")

    def delete_contact(self):
        self.show_contacts()
        data = load()
        in_data = False

        choice = input("Select name: ").strip()
        if choice == "":
            print("Name can't be empty!")
            return 
        for name, number in data.items():
            if choice == name:
                in_data = True

        if in_data == True:
            confirmation = input("Do you want to delete this contact? (y/n) ").lower().strip()
            if confirmation == "y":
                del data[name]
                save(data)
                print("<<-contact_Deleted->>")
            else:
                return   
        else:
            print("Name does not exist!")
            return

c = ContactBook()
c.save_contact()
c.delete_contact()
