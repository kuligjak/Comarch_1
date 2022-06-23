from faker import Faker
from random import randint
import csv

fake_data = Faker("pl_PL")

#
# with open("dane.csv", "w", newline="") as plik:
#     for _ in range(10):
#         line = fake_data.name() + "," + fake_data.email() + "," + fake_data.credit_card_number() + "," +\
#                fake_data.company() + "," + fake_data.ios_platform_token() + "," + fake_data.postcode()
#         print(line)
#         plik.write(line)
#         plik.write("\n")


fake_data_all = []
for _ in range(3000):
    wydatki = randint(500, 1000)
    przychody = randint(5000, 15000)
    one_row = [fake_data.name(), fake_data.email(), fake_data.credit_card_number(), wydatki, przychody]
    fake_data_all.append(one_row)

print(fake_data_all)

with open("dane2.csv", "w", newline="") as plik_csv:
    dane_writer = csv.writer(plik_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    dane_writer.writerows(fake_data_all)
