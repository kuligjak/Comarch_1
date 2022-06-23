from faker import Faker
from random import randint
import csv

fake_data = Faker("en_US")
fake_data_all = []

header = ['First_Name', 'Last_Name', 'Birth_Year', 'Country', 'City', 'Credit_Card_Provider', 'Credit_Card_Number',\
          'Credit_Card_Limit', 'Available_Limit', 'Currency_Code', 'Debt_Level']
fake_data_all.append(header)

for _ in range(9000):
    card_limit = randint(5000, 10000)
    available_limit = randint(1, 4000)
    debt_level = available_limit / card_limit

    one_row = [fake_data.first_name(), fake_data.last_name(), fake_data.year(), fake_data.country(), fake_data.city(),\
               fake_data.credit_card_provider(), fake_data.credit_card_number(), card_limit, available_limit,\
               fake_data.currency_code(), debt_level]
    fake_data_all.append(one_row)

with open("fake_dane_csv.csv", "w", newline="") as csv_file:
    dane_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    dane_writer.writerows(fake_data_all)




