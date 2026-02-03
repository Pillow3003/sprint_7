from faker import Faker


def register_new_courier():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    reg_data = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return reg_data
