from decorators import input_error
from classes import AddressBook, Record


@ input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@ input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)

    if not record:
        return "There are no record with this name"

    record.add_birthday(birthday)
    return "Birthday added."


@ input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)

    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)

    return "Contact added."


@ input_error
def change_phone(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found"

    record.edit_phone(old_phone, new_phone)

    return "Contact changed"


@ input_error
def clear_contacts(book):

    book.clear()
    return "Contacts clear"


@ input_error
def delete_record(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if not record:
        return "Contact not found"

    book.delete(name)

    return "Contact deleted"


@ input_error
def show_all(book: AddressBook):
    if not book:
        return "Book is empty"

    return book


@ input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found"
    return '; '.join(str(p) for p in record.phones)


@ input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found"
    return record.birthday


@ input_error
def birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()
