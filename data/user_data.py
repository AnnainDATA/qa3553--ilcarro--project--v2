from faker import Faker
from models.user import User

fake = Faker()

def create_user(name = None, last_name = None, email = None, password = None):
    return User(
        name = name if name is not None else fake.first_name(),
        last_name = last_name if last_name is not None else fake.last_name(),
        email = email if email is not None else fake.unique.email(),
        password = password if password is not None else fake.password(
            length=12, special_chars=True,digits=True, upper_case=True,lower_case=True
        )
    )

def existing_user():
    return create_user(
        name = "Margo",
        last_name = "Test",
        email = "anna12345@gmail.com",
        password = "123456!Anna"
    )

