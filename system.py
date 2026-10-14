from citizen import Citizen
from document import Document


class LicenseDocumentSystem:
    admin_password_hash = Citizen.hash_password("kai")

    def __init__(self):
        self.citizens = []

    def show_welcome(self):
        print("=" * 50)
        print("   WELCOME TO: License and Document Management System (LADMS)")
        print("=" * 50)

    def show_menu(self):
        print()
        print("To register a new citizen please enter 1")
        print("To register for a document please enter 2")
        print("To view existing citizens please enter 3")
        print("To view existing documents please enter 4")
        print("To exit the system please enter 5")

    def run(self):
        self.show_welcome()
        running = True
        while running:
            self.show_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.register_citizen()
            elif choice == "2":
                self.start_document_registration()
            elif choice == "3":
                self.view_citizens()
            elif choice == "4":
                self.view_documents()
            elif choice == "5":
                print("Thank you for using the Citizen's Document System. Goodbye!")
                again = input("To reopen the system enter 6 (or press Enter to close): ").strip()
                if again == "6":
                    self.show_welcome()
                else:
                    running = False
            else:
                print("Sorry, wrong input. Please enter a number from 1 to 5.")

    def find_citizen(self, citizen_id):
        for citizen in self.citizens:
            if citizen.citizen_id == citizen_id:
                return citizen
        return None

    def ask_name(self):
        while True:
            name = input("Enter your full name (or 0 to go back to the start): ").strip()
            if name == "0":
                return None
            if Citizen.is_valid_name(name):
                return " ".join(name.split())
            print("Invalid name. Use letters only and enter at least two names.")

    def ask_date_of_birth(self):
        while True:
            text = input("Enter your date of birth as DD-MM-YYYY (or 0 to go back to the start): ").strip()
            if text == "0":
                return None
            if Citizen.is_valid_date(text):
                return text
            print("Invalid date. Use the format DD-MM-YYYY, for example 25-12-2000.")

    def ask_phone_number(self):
        while True:
            phone = input("Enter your phone number (or 0 to go back to the start): ").strip()
            if phone == "0":
                return None
            if Citizen.is_valid_phone(phone):
                return phone
            print("Invalid phone number. Use digits only (8 to 13 digits, may start with +).")

    def ask_address(self):
        while True:
            address = input("Enter your address (or 0 to go back to the start): ").strip()
            if address == "0":
                return None
            if len(address) >= 3:
                return address
            print("Invalid address. Please enter characters.")

    def ask_new_password(self):
        while True:
            password = input("Create a password of at least 4 characters (or 0 to go back to the start): ").strip()
            if password == "0":
                return None
            if len(password) < 4:
                print("Password is too short. Please use at least 4 characters.")
                continue
            confirm = input("Confirm your password: ").strip()
            if confirm == password:
                return password
                print("Passwords do not match, please try again.")

    def register_citizen(self):
        print()
        print("--- CITIZEN REGISTRATION ---")
        full_name = self.ask_name()
        if full_name is None:
            return
        date_of_birth = self.ask_date_of_birth()
        if date_of_birth is None:
            return
        phone_number = self.ask_phone_number()
        if phone_number is None:
            return
        address = self.ask_address()
        if address is None:
            return
        password = self.ask_new_password()
        if password is None:
            return
        citizen = Citizen(full_name, date_of_birth, phone_number, address, password)
        self.citizens.append(citizen)
        print()
        print("You have successfully registered as a citizen.")
        print("Your Citizen ID is: " + citizen.citizen_id)
        print("Please ensure you dont forget this ID and the password you entered. You will need them to log in later on.")

    def login(self):
        citizen = None
        while citizen is None:
            citizen_id = input("Enter your citizen ID (or 0 to go back to the start): ").strip().upper()
            if citizen_id == "0":
                return None
            citizen = self.find_citizen(citizen_id)
            if citizen is None:
                print("Sorry, no citizen is registered with that ID. Please try again.")
        while True:
            password = input("Enter your password: ").strip()
            if password == "0":
                return None
            if citizen.check_password(password):
                return citizen
            print("Wrong password, please try again or enter 0 to go back to the start.")

    def start_document_registration(self):
        print()
        print("--- DOCUMENT REGISTRATION ---")
        if len(self.citizens) == 0:
            print("No registered citizen yet. Please register as a citizen first by entering 1.")
            return
        citizen = self.login()
        if citizen is None:
            return
        self.register_document(citizen)

    def register_document(self, citizen):
        print()
        print("Available documents:")
        for document_type in Document.document_types:
            print(" - " + document_type)
        while True:
            text = input("Enter the name of the document you want (or 0 to go back to the start): ").strip()
            if text == "0":
                return
            document_name = Document.find_type(text)
            if document_name == "":
                print("Sorry but this document isn't available in our system.")
            elif citizen.has_document(document_name):
                print("You have already registered for this document. Please choose another one.")
            else:
                break
        document_class = Document.get_document_class(document_name)
        field_values = []
        for label in document_class.field_labels:
            value = ""
            while value == "":
                value = input("Enter " + label + " (or 0 to go back to the start): ").strip()
                if value == "":
                    print("This field cannot be empty.")
            if value == "0":
                return
            field_values.append(value)
        document = document_class(citizen.citizen_id, field_values)
        citizen.add_document(document)
        print()
        print("Congratulations! You have successfully registered for this document (" + document_name + ").")
        print("Your document reference number is: " + document.reference_number)

    def show_citizen_names(self):
        print()
        print("REGISTERED CITIZENS")
        number = 1
        for citizen in self.citizens:
            citizen.display_name(number)
            number += 1

    def view_citizens(self):
        print()
        if len(self.citizens) == 0:
            print("No registered citizen yet.")
            return
        self.show_citizen_names()
        print()
        while True:
            password = input("To see full details enter the admin password (or 0 to go back to the start): ").strip()
            if password == "0":
                return
            if Citizen.hash_password(password) == LicenseDocumentSystem.admin_password_hash:
                break
            print("Wrong password, please try again or enter 0 to go back to the start.")
        print()
        print("FULL CITIZEN DETAILS (ADMIN VIEW)")
        Citizen.print_table_header()
        number = 1
        for citizen in self.citizens:
            citizen.display_table_row(number)
            number += 1
        print("-" * 94)

    def view_documents(self):
        print()
        if len(self.citizens) == 0:
            print("No registered citizen yet.")
            return
        self.show_citizen_names()
        print()
        print("To see your documents, log in with your citizen ID and password.")
        citizen = self.login()
        if citizen is None:
            return
        if len(citizen.documents) == 0:
            self.offer_document_registration(citizen)
        else:
            print()
            citizen.display_documents()

    def offer_document_registration(self, citizen):
        print()
        print("No document registered yet.")
        while True:
            choice = input("Enter 2 to register a document (or 0 to go back to the start): ").strip()
            if choice == "2":
                self.register_document(citizen)
                return
            if choice == "0":
                return
            print("Sorry, wrong input, please enter 2.")