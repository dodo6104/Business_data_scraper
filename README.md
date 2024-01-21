This project was created to furnish the client with company data for their marketing endeavors. It's crucial to highlight that the entire scraping process was carried out using publicly available sources, rendering it an ethically sound project. This implies that the information retrieval adhered to ethical standards and refrained from breaching privacy or accessing sensitive non-public data.
This project entails an automated process for extracting data from the Self Storage Association's website, which houses information about self-storage companies globally. The project workflow is outlined as follows:

Reading the list of countries:
-->The list of countries is read from the "countries.txt" file.

Initializing an empty data list:
-->data is initialized as an empty list to store information about found self-storage facilities.

Iterating through the list of countries:
-->For each country in the list, the following steps are performed:

Initializing a web browser using Selenium:
-->Selenium is used to automate a web browser (Google Chrome in headless mode) for accessing the Self Storage Association's page for the given country.

Opening the web page for the specific country:
-->The content of the page is loaded using the link for the respective country on the Self Storage Association's page.

Analyzing the page using BeautifulSoup:
-->BeautifulSoup is employed to parse the HTML content of the page and extract information about self-storage facilities.

Processing the page content and extracting information:
-->The content of the page is traversed, and information such as company name, website, address, phone number, and email of the self-storage facility is extracted.