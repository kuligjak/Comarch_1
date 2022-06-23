def simple_print():
    print("To jest prosta funkcja")


def simple_return():
    print(f"This is simple return statement...")
    return "ZWRACAMY"

def is_pallindrome(word):
    print(f"Sprawdzam słowo {word}")
    return word == word[::-1]


def simple_bmi(waga, wzrost):
    bmi = waga / wzrost ** 2
    print(f"BMI wynosi {bmi}")
    return bmi


moje_bmi = simple_bmi(88, 1.86)
if moje_bmi < 20:
    print("Super")
else:
    print("Idź do lekarza")

# print(is_pallindrome("KAMILŚLIMAK"))
# simple_print()
#
# x = simple_return()
# print(x)