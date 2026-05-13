from structure import ContactBook

class Main(ContactBook):
    def menu(self):
        while True:
            print("<<--Contact Book->>")
            print("1. Add a contact")
            print("2. Show all contacts")
            print("3. Search a contact")
            print("4. Update a contact")
            print("5. Delete a contact")
            print("6. Exit")

            choice = input("Enter choice: ").strip()
            if choice == "":
                print("choice can't be empty!")
                return
                
            if choice == "1":
                print("\n")
                self.save_contact()
                print("\n")
                
            elif choice == "2":
                print("\n")
                self.show_contacts()
                print("\n")
                
            elif choice == "3":
                print("\n")
                self.search_contact()
                print("\n")
                
            elif choice == "4":
                print("\n")
                self.update_contact()
                print("\n")
                
            elif choice == "5":
                print("\n")
                self.delete_contact()
                print("\n")
            elif choice == "6":
                print("\nGoodBye!")
                break

            else:
                print("Invalid choice! choose from 1 to 6.")


main = Main()
main.menu()
    
