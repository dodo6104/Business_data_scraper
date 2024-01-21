from bs4 import BeautifulSoup
from selenium import webdriver
import openpyxl

# Read the list of countries: Load the list of countries from the "countries.txt" text file and store it in the "countries" variable.
countries = []
with open('Input/countries.txt', 'r') as file:
    countries = file.readlines()

# Initialize an empty "data" list: This list will be used to store information about found self-storage facilities.
data = [["Name Of Business", "Web", "Address", "Country", "Phone", "Email"]]

# Iterate through the list of countries: For each country in the list, perform the following steps:
for country in countries:
    # Initialize a web browser using Selenium with "headless" mode, which means the browser will operate without a graphical interface.
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    print(country)

    # Open the Self Storage Association's web page for the given country.
    driver.get(f"https://www.selfstorage.org/cvweb/cgi-bin/utilities.dll/CustomList?O.ORGNAME=~~&O.COUNTRY={country}&RANGE=1/1000000&O.ISMEMBERFLG=Y&O.NOWEBFLG=%3C%3EY&O.STATUSSTT=Active&SHOWSQL=N&WHP=dir_facility.htm&WBP=dir_facility_list.htm&SORT=ORGNAME&QNAME=FACILITYNODISTANCE")

    # Analyze the page using BeautifulSoup: Process the HTML content of the page and retrieve information about self-storage facilities.
    soup = BeautifulSoup(driver.page_source, 'lxml')

    try:
        # Process the page content to extract information about the facilities.
        div = soup.find('div', id="siteContent").find('div').find_all("div")
        for d in div:
            name = None
            website = None
            address = None
            phone = None
            email = None

            # Get the company name if available.
            try:
                name = d.find('p').find('a').text
            except Exception:
                pass

            # Get the company's website if available.
            try:
                website = d.find('a', {'class': 'wwwlink hideIfBlanksentry-selfstorage.com'})['href']
            except Exception:
                pass

            # Get the company's address if available.
            try:
                address = d.find_all('p')[1].text
            except Exception:
                pass

            # Get the company's phone number if available.
            try:
                phone = d.find_all('p')[2].find('strong').next_sibling.strip()
            except Exception:
                pass

            # Get the company's email address if available.
            try:
                email_element = d.find('p', {'class': 'hidden hide'})
                if email_element:
                    email = email_element.find('a')['href'].replace('mailto:', '')
            except Exception:
                pass

            # Add the found company information to the "data" list.
            data.append([name, website, address, country, phone, email])
    except Exception:
        pass

    # Close the web browser.
    driver.quit()

# Create an Excel file: Initialize a new Excel file and create an active sheet.
workbook = openpyxl.Workbook()
sheet = workbook.active

# Save data to the Excel file: Iterate through the "data" list and add individual rows to the Excel file.
for row in data:
    sheet.append(row)

# Save the Excel file.
workbook.save("Output/output.xlsx")
