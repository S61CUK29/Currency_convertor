import requests
import json

def get_exchange_rates(base_currency):
    """Fetch current exchange rates from API"""
    try:
        url = f"https://api.frankfurter.app/latest?from={base_currency}"
        response = requests.get(url)
        response.raise_for_status()  # Raises exception for HTTP errors
        data = response.json()
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency):
    """Convert an amount from one currency to another"""
    if from_currency == to_currency:
        return amount
    
    rates = get_exchange_rates(from_currency)
    
    if rates is None:
        return None
    
    if to_currency in rates:
        return amount * rates[to_currency]
    else:
        print(f"Currency {to_currency} not supported")
        return None

def get_user_amount():
    """Safely get amount from user with error handling"""
    while True:
        try:
            return float(input("Enter amount to convert: "))
        except ValueError:
            print("Please enter a valid number")

def get_user_currency(prompt):
    """Safely get currency code from user"""
    while True:
        currency = input(prompt).upper()
        if len(currency) == 3 and currency.isalpha():
            return currency
        print("Please enter a valid 3-letter currency code (e.g., USD, EUR)")

def main():
    print("Welcome to Currency Converter!")
    
    while True:
        print("\nOptions:")
        print("1. Convert currencies")
        print("2. List available currencies")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            amount = get_user_amount()
            from_curr = get_user_currency("From currency (3-letter code): ")
            to_curr = get_user_currency("To currency (3-letter code): ")
            
            result = convert_currency(amount, from_curr, to_curr)
            if result is not None:
                print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
        
        elif choice == "2":
            print("Common currencies: USD, EUR, GBP, JPY, CAD, AUD, CNY, INR")
            print("For full list, visit: https://api.frankfurter.app/currencies")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()