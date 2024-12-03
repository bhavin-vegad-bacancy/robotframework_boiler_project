from faker import Faker
fake = Faker()

def generate_fake_name():
    firstname = fake.name()
    return firstname

def generate_fake_email():
    email = fake.email()
    return email

def generate_fake_phone_number():
    phone_number = fake.phone_number()
    return phone_number

def generate_fake_address():
    address = fake.address()
    return address