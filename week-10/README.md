Country Explorer (by Region)

A command-line tool for exploring countries by region. Fetch country data from the REST Countries API, view general information (description, population, government structure), and filter countries by international memberships (EU, NATO, etc.)

_ _ _ _ _ _ _

API used: "https://api.restcountries.com/countries/v5"

API key: required, free to obtain on the website: https://restcountries.com/docs/countries

Key handling: stored in .env file, read via "COUNTRY_API_KEY" environment variable

The project requires installation of your own .env file
_ _ _ _ _ _ _

Requirements

Required: Python Python 3.14.6 or greater installed. 

Dependencies: install with pip install -r requirements.txt

Required: 
python-dotenv==1.2.3
requests==2.34.2

_ _ _ _ _ _ _

How To Run: python project.py

The program presents a looping menu:
=== Country Explorer (by Region) ===
1. Get general country information
2. Filter by membership
3. Quit

Choose an option (1-3)

Option 1: Input a region (Europe, Asia, etc.). The program fetches all countries and prints: country name, short description, population, government type

Option 2: Prompts for a region and then shows a menu of international organizations. Input numbers separated by spaces. THe program matches the countries that are members and prints their names.

OPtion 3: Quit