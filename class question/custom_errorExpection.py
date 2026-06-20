class invalidAgeError(Exception):

    def __int__(self,age,message="Age must be 18 or above"):
        self.age=age
        self.message=message
        super.__init__(f"{message}.Given age:{age}")
def register_user(age):
    if age<18:
        raise InavlidAgeError(age)
    print("User Registered successfully")
try:
    register_user(15)
except InvalidAgeError as e:
    print(f"Error:{e}")
