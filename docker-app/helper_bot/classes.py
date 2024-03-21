from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError(
                "Number must have 10 numbers and contain only digits")

    def __str__(self):
        return str(self.value)


class Record(Field):
    def __init__(self, name):

        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)
        

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError
      
          

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}, birthday: {str(self.birthday)}"


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except:
            raise ValueError


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        date_today = datetime.today().date()
        birthdays = []
        for name, record in self.data.items():
            birth_date = record.birthday.value.replace(year=date_today.year)

            week_day = birth_date.isoweekday()
            days_between = (birth_date - date_today).days
            if 0 <= days_between < 8:
                if week_day < 6:
                    birthdays.append(
                        {'name': name, 'birthday': birth_date.strftime("%Y.%m.%d")})

                else:
                    birthdays.append({'name': name, 'birthday': (
                        birth_date + timedelta(days=8 - week_day)).strftime("%Y.%m.%d")})

        return birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
