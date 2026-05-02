def validate_signup(func):
    def wrapper(first_name, last_name,  contact, password, confirm_password):
        
        # First Name
        if not first_name or not isinstance(first_name, str):
            return "First name must be a non-empty string"

        # Last Name
        if not last_name or not isinstance(last_name, str):
            return "Last name must be a non-empty string"

        

        # Contact Number
        if len(contact) != 10 or not contact.isdigit():
            return "Contact must be 10 digit number"

        # Password
        if len(password) < 6:
            return "Password must be at least 6 characters"

        # Confirm Password
        if password != confirm_password:
            return "Passwords do not match"

        return func(first_name, last_name, contact, password, confirm_password)

    return wrapper


@validate_signup
def signup(first_name, last_name,  contact, password, confirm_password):
    return f"Signup successful Welcome {first_name} {last_name}!"
print(signup("vikas","kannojiya","1238903325","123456","234567"))
print(signup("","kannojiya","1238903325","123456","234567"))
