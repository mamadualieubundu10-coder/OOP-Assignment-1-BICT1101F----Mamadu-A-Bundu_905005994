from datetime import date


class Document:
    document_types = (
        "National ID",
        "Birth Certificate",
        "Death Certificate",
        "Driver's License",
        "Passport",
        "Voter ID Card",
        "NASSIT Card",
    )
    field_labels = ()
    total_documents = 0

    def __init__(self, owner_id, document_name, field_values):
        self.owner_id = owner_id
        self.document_name = document_name
        self.field_values = field_values
        self.reference_number = Document.generate_reference_number()
        self.date_registered = date.today().strftime("%d-%m-%Y")

    @classmethod
    def generate_reference_number(cls):
        Document.total_documents += 1
        return "DOC-" + str(Document.total_documents).zfill(4)

    @staticmethod
    def find_type(text):
        cleaned = " ".join(text.lower().replace("'", "").replace("\u2019", "").split())
        for document_type in Document.document_types:
            if document_type.lower().replace("'", "") == cleaned:
                return document_type
        return ""

    @staticmethod
    def get_document_class(document_name):
        if document_name == "National ID":
            return NationalID
        if document_name == "Birth Certificate":
            return BirthCertificate
        if document_name == "Death Certificate":
            return DeathCertificate
        if document_name == "Driver's License":
            return DriversLicense
        if document_name == "Passport":
            return Passport
        if document_name == "Voter ID Card":
            return VoterIDCard
        if document_name == "NASSIT Card":
            return NassitCard
        return None

    def display_info(self):
        print("Document Type    : " + self.document_name)
        print("Reference Number : " + self.reference_number)
        print("Owner ID         : " + self.owner_id)
        print("Date Registered  : " + self.date_registered)
        for label, value in zip(self.field_labels, self.field_values):
            print(label.ljust(17) + ": " + value)
        print("-" * 50)


class NationalID(Document):
    field_labels = ("Gender", "Place of Birth", "Occupation")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "National ID", field_values)

    def display_info(self):
        print("Issued By        : National Civil Registration Authority (NCRA)")
        super().display_info()


class BirthCertificate(Document):
    field_labels = ("Gender", "Place of Birth", "Father's Name", "Mother's Name")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "Birth Certificate", field_values)

    def display_info(self):
        print("Issued By        : National Civil Registration Authority (NCRA)")
        super().display_info()


class DeathCertificate(Document):
    field_labels = ("Date of Death", "Place of Death", "Informant's Name")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "Death Certificate", field_values)

    def display_info(self):
        print("Issued By        : National Civil Registration Authority (NCRA)")
        super().display_info()


class DriversLicense(Document):
    field_labels = ("License Class", "Date of Issue", "Expiry Date")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "Driver's License", field_values)

    def display_info(self):
        print("Issued By        : Sierra Leone Road Safety Authority (SLRSA)")
        super().display_info()


class Passport(Document):
    field_labels = ("Place of Birth", "Nationality", "Date of Issue", "Expiry Date")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "Passport", field_values)

    def display_info(self):
        print("Issued By        : Sierra Leone Immigration Department")
        super().display_info()


class VoterIDCard(Document):
    field_labels = ("Constituency", "Ward", "Polling Station")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "Voter ID Card", field_values)

    def display_info(self):
        print("Issued By        : Electoral Commission for Sierra Leone (ECSL)")
        super().display_info()


class NassitCard(Document):
    field_labels = ("Employer's Name", "Date of Employment")

    def __init__(self, owner_id, field_values):
        super().__init__(owner_id, "NASSIT Card", field_values)

    def display_info(self):
        print("Issued By        : National Social Security and Insurance Trust (NASSIT)")
        super().display_info()