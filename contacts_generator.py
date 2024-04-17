import os
import sys
from faker import Faker

def generate_vcard(fake):
    last_name = fake.last_name()
    first_name = fake.first_name()
    prefix = fake.prefix()
    company = fake.company()
    title = fake.job()
    phone_number = fake.phone_number()
    email = fake.ascii_email()
    return f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;{prefix};
FN:{first_name} {last_name}
ORG:{company}
TITLE:{title}
TEL;TYPE=cell,voice:{phone_number}
EMAIL:{email}
END:VCARD
"""

def create_file(num_contacts):
    fake = Faker()
    with open("contacts.vcf", "a") as file:
        for _ in range(num_contacts):
            vcard_content = generate_vcard(fake)
            file.write(vcard_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <num_contacts>")
        sys.exit(1)
    try:
        num_contacts = int(sys.argv[1])
    except ValueError:
        print("Error: <num_contacts> must be an integer")
        sys.exit(1)
    create_file(num_contacts)
