# READ ME

# License and Document Management System (LADMS)

## Overview

LADMS is a console application written in Python using Object-Oriented Programming. It addresses a practical government need: recording citizens and tracking the official documents and licenses that are issued to them. The project falls under the Government domain, acting as a Digital Permit and License Management System.

A citizen signs up and is given an automatically created citizen ID (for instance CDS-0001). Once registered, the citizen can add documents, and every document is assigned its own reference number. The supported documents are the National ID, Birth Certificate, Death Certificate, Driver's License, Passport, Voter ID Card and NASSIT Card.

## Key Features

- Sign up a new citizen using a full name, date of birth, phone number, address and password
- Automatic creation of the citizen ID, document reference numbers and age
- Add documents, with input fields tailored to each document type
- A public list that shows citizen names only
- Complete citizen records displayed in a table, available only with the admin password
- A citizen's documents displayed only after entering their own ID and password
- Input validation with clear feedback, for example "Wrong password, please try again or enter 0 to go back to the start."
- Protection against duplicates: a citizen cannot add the same type of document twice

## Alignment with Digital Public Goods (DPG) Standards

- **Open-source:** the complete source code is published on GitHub, so anyone is free to read, run and improve it.
- **Inclusive and accessible:** the program relies on simple text menus and easy-to-understand prompts. It works offline, requires nothing beyond Python, and needs no special hardware. Entering 0 on any screen takes the user back, and every invalid entry produces a helpful message.
- **Privacy-respecting:** all data lives in memory only, and nothing is saved to a file or sent elsewhere. Passwords are never kept as plain text; only a SHA-256 hash is stored. The public view lists names only, full details require the admin password, and documents require the citizen's own ID and password.
- **Modular and reusable:** the code is divided into separate files, and each class can be reused in other projects.

## OOP Concepts Applied

| Concept | Where it is used |
|---|---|
| Classes, attributes and objects | Citizen, Document and LicenseDocumentSystem |
| Data structure: list | self.citizens in system.py, and self.documents in citizen.py |
| Tuples | document_types and field_labels in document.py |
| Instance methods | get_age, check_password, has_document, add_document |
| Class methods | generate_citizen_id, generate_reference_number |
| Static methods | hash_password, calculate_age, find_type |
| Inheritance and polymorphism | Seven document classes inherit from Document and override display_info |
| Encapsulation | Private __password_hash |

## Project Layout

- **main.py:** the entry point that launches the program
- **system.py:** the menus, input handling and validation, plus the list of citizens
- **citizen.py:** the Citizen class
- **document.py:** the Document base class and its seven subclasses

## Running the Program

1. Make sure Python 3.8 or later is installed. No additional libraries are required.
2. Save all four .py files together in one folder.
3. Open a terminal inside that folder and type: `python main.py`



## Author

**Author's name:** Mamadu A Bundu

<<<<<<< HEAD
**Student ID:** 905005994

