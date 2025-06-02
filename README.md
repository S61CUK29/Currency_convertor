 Currency Converter – Python CLI App
This is a simple Python command-line application that converts an amount from one currency to another using real-time exchange rates from the Frankfurter API.

 Features:
Convert an amount between two currencies (e.g., USD → EUR).

List some commonly used currency codes.

Error handling for:

Invalid user inputs (amounts, currency codes).

Network/API issues.

Unsupported currencies.

 Dependencies:
requests – for HTTP requests to the API.

Install via pip if not already available:

bash
Copy
Edit
pip install requests
 How It Works:
User selects an option from the menu.

If converting currency:

Inputs the amount and currency codes (e.g., USD, EUR).

The app fetches exchange rates and calculates the converted amount.

Displays results or helpful error messages.

Optionally, lists common currencies or exits the program.

 Example Usage:
vbnet
Copy
Edit
Welcome to Currency Converter!

Options:
1. Convert currencies
2. List available currencies
3. Exit
Enter your choice (1-3): 1
Enter amount to convert: 100
From currency (3-letter code): USD
To currency (3-letter code): EUR
100 USD = 92.50 EUR
