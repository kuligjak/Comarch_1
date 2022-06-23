def read_float(message):
    value = None
    while value is None:
        value = input(message)
        try:
            value = int(value)
            return value
        except:
            try:
                value = float(value)
                return value
            except:
                print("Not int or float")
                value = None
    return value


def read_client_data(client_name):
    months = int(input("How many months? "))
    clients_payments = []  # lista
    client_data = {
        "payments": [],
        "avg_payment": None,
        "next_payment": None,
    }

    for month in range(months):
        payment = read_float(f"Payment for month {month}: ")
        # payment = float(input(f"Payment for month {month} : "))
        clients_payments.append(payment)

    print(f"Payments for last {months} months for client {client_name} are: {clients_payments}")

    client_data["payments"] = clients_payments
    client_data["avg_payment"] = sum(clients_payments) / months
    client_data["next_payment"] = client_data["avg_payment"] * 1.06

    return client_data
