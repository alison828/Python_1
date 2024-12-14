
def currency_converter():
    # Predefined exchange rates to USD
    exchange_rates_to_usd = {
        "ARS": 1012.00,  # 1 USD = 1012.00 ARS
        "EUR": 0.9460075,  # 1 USD = 0.9460075 EUR
        "COP": 4409.3044  # 1 USD = 4409.3044 COP
    }

    while True:  # Loop to handle invalid inputs
        try:
            # Input: Ask the user for the base currency
            base_currency = input("Enter the currency you want to convert to USD (ARS, EUR, COP): ")
            if base_currency not in exchange_rates_to_usd:
                raise ValueError("Invalid currency. Please choose from ARS, EUR, or COP.")

            # Input: Ask for the amount in the base currency
            amount = float(input(f"Enter the amount in {base_currency}: "))
            if amount < 0:
                raise ValueError("Amount must be a positive number.")

            # Processing: Convert the amount to USD
            rate = exchange_rates_to_usd[base_currency]
            converted_amount = amount / rate

            # Output: Display the converted amount in USD
            print(f"{amount:.2f} {base_currency} is equal to {converted_amount:.2f} USD.")
            break  # Exit the loop after successful conversion

        except ValueError as e:
            # Handle invalid input and display error message
            print(f"Error: {e}. Please try again.")

# Call the function
currency_converter()






