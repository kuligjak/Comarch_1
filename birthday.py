my_name = input("Jak masz na imię? ")
my_birth = int(input(f"{my_name}, podaj Twój rok urodzenia? "))
actual_year = 2022
my_age = actual_year - my_birth
# F-String
print(f"Siemanko {my_name}, ja jestem Python")
print(f"W roku {actual_year} masz {my_age} lat")

if my_age >= 18:
    print(f"V.1 Hej {my_name} - jesteś {'dorosła' if my_name.endswith('a') else 'dorosły'}")
    if my_name.endswith('a'):
        gender = 'a'
    else:
        gender = 'y'

    print(f"Hej, {my_name} - jesteś dorosł{gender}!")
    print("Możesz kupić piwo!")
else:
    print(f"Do dorosłości brakuje Ci {18 - my_age} lat.")

