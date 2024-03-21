

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return "There are no contact with this name."

        except ValueError:
            return "Give me name and phone with correct value please"

        except IndexError:
            return "Index error"

    return inner
