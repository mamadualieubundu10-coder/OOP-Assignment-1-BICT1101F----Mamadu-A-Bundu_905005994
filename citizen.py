import hashlib
from datetime import date


class Citizen:
    total_citizens = 0

    def __init__(self, full_name, date_of_birth, phone_number, address, password):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.address = address
        self.citizen_id = Citizen.generate_citizen_id()
        self.__password_hash = Citizen.hash_password(password)
        self.documents = []

    @classmethod
    def generate_citizen_id(cls):
        cls.total_citizens += 1
        return "CDS-" + str(cls.total_citizens).zfill(4)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def is_valid_name(name):
        letters = 0
        for character in name:
            if character.isalpha():
                letters += 1
            elif character not in " -'":
                return False
        return letters >= 2 and len(name.split()) >= 2

    @staticmethod
    def is_valid_phone(phone):
        digits = phone
        if phone.startswith("+"):
            digits = phone[1:]
        return digits.isdecimal() and 8 <= len(digits) <= 13

    @staticmethod
    def is_valid_date(text):
        parts = text.split("-")
        if len(parts) != 3:
            return False
        day_text = parts[0]
        month_text = parts[1]
        year_text = parts[2]
        if not (day_text.isdecimal() and month_text.isdecimal() and year_text.isdecimal()):
            return False
        if len(day_text) != 2 or len(month_text) != 2 or len(year_text) != 4:
            return False
        day = int(day_text)
        month = int(month_text)
        year = int(year_text)
        if year < 1900 or month < 1 or month > 12:
            return False
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[1] = 29
        if day < 1 or day > days_in_month[month - 1]:
            return False
        if date(year, month, day) > date.today():
            return False
        return True

    @staticmethod
    def calculate_age(date_of_birth):
        parts = date_of_birth.split("-")
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        today = date.today()
        age = today.year - year
        if (today.month, today.day) < (month, day):
            age -= 1
        return age

    def get_age(self):
        return Citizen.calculate_age(self.date_of_birth)

    def check_password(self, entered_password):
        return Citizen.hash_password(entered_password) == self.__password_hash

    def has_document(self, document_name):
        for document in self.documents:
            if document.document_name == document_name:
                return True
        return False

    def add_document(self, document):
        self.documents.append(document)

    def display_name(self, number):
        print(str(number) + ". " + self.full_name)

    @staticmethod
    def print_table_header():
        header = f"{'No.':<4}{'ID':<10}{'Full Name':<22}{'Date of Birth':<14}{'Age':<5}{'Phone':<15}{'Address':<20}{'Docs':<4}"
        print(header)
        print("-" * len(header))

    def display_table_row(self, number):
        print(f"{number:<4}{self.citizen_id:<10}{self.full_name:<22.21}{self.date_of_birth:<14}{str(self.get_age()):<5}{self.phone_number:<15}{self.address:<20.19}{len(self.documents):<4}")

    def display_documents(self):
        print("=" * 50)
        print("DOCUMENTS OF " + self.full_name.upper() + " (" + self.citizen_id + ")")
        print("=" * 50)
        for document in self.documents:
            document.display_info()