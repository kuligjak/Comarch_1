from payments_functions.read_data import *
from other_functions.finanse import *

our_clients = {}  # słownik

while True:
    client_name = input("Please tell me name of the client: ")
    if client_name == 'STOP':
        break

    our_clients[client_name] = read_client_data(client_name)
    print(f"{client_name} data: {our_clients[client_name]}")
    tmp_data = our_clients[client_name]
    income = tmp_data["payments"]
    print(f"Income: {income}")
    tmp_data["next_payment"] = avg_income(income)
    print(f"Values after: {tmp_data}")

print(f"Our full database: {our_clients}")

