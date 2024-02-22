from faker import Faker
import pandas as pd

fake = Faker()

name = []
country = []
phone = []
credit_card = []
provider_card = []
security_code = []

for _ in range(350):
    name_data = fake.name()
    name.append(name_data)

    creditCard_data = fake.credit_card_number()
    credit_card.append(creditCard_data)

    providerCard_data = fake.credit_card_provider()
    provider_card.append(providerCard_data)

    securityCode_data = fake.credit_card_security_code()
    security_code.append(securityCode_data)

    country_data = fake.country()
    country.append(country_data)

    phone_data = fake.phone_number()
    phone.append(phone_data)

df = pd.DataFrame(list(zip(name, credit_card, provider_card, security_code, country, phone)), columns=["name","credit_card_number","credit_card_provider","security_code","country","phone"])
print(df)