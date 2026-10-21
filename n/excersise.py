
"""
country = "Italy"

while True:

    user_input = input("Please enter a country: ")

    match user_input:

        case "USA":
            print("Hello")
        case "Italy":
            print("Ciao")
        case "Germany":
            print("Hallo")
"""

country = []

while True:

    user_input = input("Please enter a country: ")
    country.append(user_input)
    match user_input:

        case "USA":
            print("Hello")
        case "Italy":
            print("Ciao")
        case "Germany":
            print("Hallo")
