from handlers import parse_input, add_contact, show_all, change_phone, show_phone, delete_record, clear_contacts, birthdays, add_birthday, show_birthday
from classes import AddressBook
from serialization import save_data, load_data


def main():
    book = AddressBook()
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "delete":
            print(delete_record(args, book))

        elif command == "clear":
            print(clear_contacts(book))

        elif command == "birthdays":
            print(birthdays(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
