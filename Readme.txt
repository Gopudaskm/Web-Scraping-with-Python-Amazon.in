#Amazon Web Scraper

This is a Python script that scrapes product details of Air Conditioners from Amazon.in and saves the data in a CSV file named Amazon_data1.csv. 
This script is for educational purposes only.

Required Libraries
*requests
*lxml
*beautifulsoup4
*csv
*datetime
*time

To run the script, execute the following command in your terminal:
python amazon_scrape.py

The script will scrape the data from the following Amazon page: https://www.amazon.in/s?i=kitchen&rh=n%3A3474656031&fs=true&ref=sr_pg_1

The script will extract the following product details: title, M.R.P, price, savings(%), brand, model, capacity, Annual Energy Consumption, and link for the product. 
The data will be saved in a CSV file named Amazon_data1.csv with the current date.

Disclaimer
This script is for educational purposes only. The use of this script for any other purpose is not recommended and is entirely at your own risk. 
The author is not responsible for any consequences resulting from the use of this script.

#Amazon Data Cleaning

This is a Python script that cleans the product details data extracted from Amazon using the script 'amazon_scrape.py'.
 The script uses the pandas library to clean the data and saves the cleaned data in a CSV file named 'Amazon_data2.csv'.

Required Libraries
pandas


To run the script, execute the following command in your terminal:

python amazon_clean.py

The script will read the data from the CSV file named 'Amazon_data1.csv' and clean the data using the pandas library. 
The cleaned data will be saved in a CSV file named 'Amazon_data2.csv' with the current date.

The script performs the following data cleaning operations:

Removing any duplicate rows
Removing any rows with missing values
Removing any rows with invalid data
Converting the data types of the columns to the appropriate data type


