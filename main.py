from password_generator import generate_password
import storage

def menu():
    print("Welcome to Othniel's Password Manager App")

    while True:
        print("\n--- Password Manager ---")
        print("1. Generate Password")
        print("2. Add Credentials")
        print("3. Retrieve Credentials")
        print("4. Delete Credentials")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("\nEnter Password Length: "))
            print("Generate Password: ", generate_password(length))

        elif choice == "2":
            website = input("\nEnter website/app name: ").lower()
            username = input("Enter username/email: ").lower()
            password = input("Enter password (leave blank to auto-generate): ")

            if not password:
                password = generate_password()
            storage.add_credentials(website, username, password)
            print("Credentials saved successfully!")
        
        elif choice == "3":
            website = input("\nEnter website/app name: ")
            credentials = storage.get_credentials(website)
            if credentials:
                print(f"Username: {credentials['username']}\nPassword: {credentials['password']}")
            else:
                print("No credentials found.")
        
        elif choice == "4":
            website = input("\nEnter website/app name: ")
            if storage.delete_credentials(website):
                print("Credentials deleted successfully.")
            else:
                print("No credentials found.")
        
        elif choice == "5":
            print("\nExiting... Goodbye")
            break
        
        else:
            print("\nInvalid choice, try again!")
    
if __name__ == "__main__":
    menu()
