def validate_name_and_contact(func):
    def wrapper(name,contact_number):
        if not name or not isinstance(name,str):
            return "name must be a non empty string."
        if len(contact_number)!=10 or not contact_number.isdigit():
            return "contact number must be a 10 digit number"

        return func(name,contact_number)
    return wrapper
@validate_name_and_contact
def register_user(name,contact_number):
    return f"user{name} must with numb{contact_number} has been ."
print(register_user("vikas" ,"123456790"))
