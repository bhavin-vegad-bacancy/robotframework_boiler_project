import csv
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define the number of records
num_records = 50

# Write data to CSV file with UTF-8 encoding
csv_file = "fake_data.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=[
        "Name", "Address", "Email", "Phone Number", "Social Security Number", "Date of Birth",
        "Age", "Username", "Password", "Lorem Ipsum Text", "Sentence", "Paragraph",
        "Random Integer", "Random Float", "Random Percentage", "Random Date", "Random Time",
        "Random Datetime", "Timezone", "URL", "Domain Name", "IPv4 Address", "IPv6 Address",
        "User Agent", "MAC Address", "Company Name", "Job Title", "Credit Card Number",
        "Credit Card Expiration Date", "Credit Card Security Code", "Latitude", "Longitude",
        "Color Name", "Hex Color", "File Name", "File Extension", "Boolean Value", "UUID",
        "Language", "Country", "Currency"
    ])
    writer.writeheader()

    for _ in range(num_records):
        data = {
            "Name": fake.name(),
            "Address": fake.address(),
            "Email": fake.email(),
            "Phone Number": fake.phone_number(),
            "Social Security Number": fake.ssn(),
            "Date of Birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "Age": fake.random_int(min=18, max=90),
            "Username": fake.user_name(),
            "Password": fake.password(length=8),  # Default password length is 8
            "Lorem Ipsum Text": fake.text(),
            "Sentence": fake.sentence(),
            "Paragraph": fake.paragraph(),
            "Random Integer": fake.random_int(),
            "Random Float": fake.random_number(digits=2),  # Default number of digits is 10
            "Random Percentage": fake.random_element(elements=(10, 20, 30, 40, 50)),
            "Random Date": fake.date(),
            "Random Time": fake.time(),
            "Random Datetime": fake.date_time(),
            "Timezone": fake.timezone(),
            "URL": fake.url(),
            "Domain Name": fake.domain_name(),
            "IPv4 Address": fake.ipv4(),
            "IPv6 Address": fake.ipv6(),
            "User Agent": fake.user_agent(),
            "MAC Address": fake.mac_address(),
            "Company Name": fake.company(),
            "Job Title": fake.job(),
            "Credit Card Number": fake.credit_card_number(card_type=None),
            "Credit Card Expiration Date": fake.credit_card_expire(),
            "Credit Card Security Code": fake.credit_card_security_code(),
            "Latitude": fake.latitude(),
            "Longitude": fake.longitude(),
            "Color Name": fake.color_name(),
            "Hex Color": fake.hex_color(),
            "File Name": fake.file_name(extension=None),  # Default extension is None
            "File Extension": fake.file_extension(),
            "Boolean Value": fake.boolean(chance_of_getting_true=50),  # Default chance is 50%
            "UUID": fake.uuid4(),
            "Language": fake.language_code(),
            "Country": fake.country(),
            "Currency": fake.currency_name()
        }
        writer.writerow(data)

print(f"Data written to {csv_file}")
