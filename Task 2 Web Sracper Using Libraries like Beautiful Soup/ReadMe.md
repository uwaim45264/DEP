# Web Scraper Application

This is a Python-based GUI application for web scraping using `customtkinter`, `requests`, and `BeautifulSoup`. The application allows users to input a URL and a CSS selector to scrape specific elements from the webpage and save the extracted data into a CSV file.

## Features

- Input URL and CSS selector to scrape data from web pages.
- Extract text content from the specified elements.
- Save the scraped data to a CSV file.

## Requirements

- Python 3.x
- `customtkinter` library
- `requests` library
- `BeautifulSoup` library
- `csv` (standard library)
- `tkinter` (standard library)

## Installation

Install the required libraries:

You can install the required libraries using pip:

pip install customtkinter requests beautifulsoup4

Usage
Run the application:

python web_scraper.py

Input the URL and CSS selector:

Enter the URL of the webpage you want to scrape in the URL field.
Enter the CSS selector for the elements you want to scrape in the CSS Selector field.
Save the data:

Click the "Save as" button.
Choose the location and name for the CSV file where the scraped data will be saved.
Code Overview
The application is structured as follows:

scrape_and_save(): This function performs the web scraping and saves the data to a CSV file.

Makes an HTTP request to the provided URL.
Parses the HTML content using BeautifulSoup.
Extracts text from the elements specified by the CSS selector.
Prompts the user to choose a location to save the CSV file.
Saves the extracted data to the CSV file.
GUI Elements:

Labels: url_label, lable (title), selector_label, developer_name_lable
Entry Widgets: url_entry, selector_entry
Button: scrape_button

Developer
Developed by MUHAMMAD UWAIM QURESHI
