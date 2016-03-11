"""
First, we'll import several standard library modules to use. These are some of the most frequently used libaries
in Python. Also, these three double quotes--you can use single quotes too--create a multi-line string. It's great
For adding a large comment like this one or for setting a variable to a large block of text.
"""
import os
import csv
import json


# Use the os module to 
file_name = "marijuana_gross_sales.csv"
file_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data', file_name))

# Open the csv
csv_file = open(file_path, 'rb')

# Create the object that represents the data in the csv file
csv_data = csv.reader(csv_file)

# Create a variable to represent the header row
header_row = csv_data.next()  # explain generators

# transforming data
data = list(csv_data)

# analyze data
all_gross_income = [d[3] for d in data]
# sum(all_gross_income)  # this will fail
def list_to_dict(alist):
	# alist vs list
	return dict( zip(header_row, alist) )

list_to_dict = lambda alist: dict( zip(header_row, alist) )

data_dict = [list_to_dict(d) for d in data]

for d in data_dict:
	d['GROSS_SALES'] = float(d['GROSS_SALES'])
	d['MONTH'] = d['MONTH'].strip()

all_gross_income = [d['GROSS_SALES'] for d in data_dict]  # reads better!

average_gross_income =  sum(all_gross_income) / len(all_gross_income)

data_2015 = [d for d in data_dict if d['YEAR'] == '2015']
all_gross_income_2015 = [d['GROSS_SALES'] for d in data_2015]
average_gross_income_2015 = sum(all_gross_income_2015) / len(all_gross_income_2015)

# data_2014 = [d for d in data if d[0] == '2014']
# all_gross_income_2014 = [float(d[3]) for d in data_2014]
# average_gross_income_2014 = sum(all_gross_income_2014) / len(all_gross_income_2014)

# def turn_value_to_float(value):
# 	return float(value)

# lambda value:float(value)

largest_sale = max(data_dict, key=lambda x:float(x['GROSS_SALES']))
smallest_sale = min(data_dict, key=lambda x:float(x['GROSS_SALES']))

pct_of_sales = largest_sale['GROSS_SALES'] / sum(all_gross_income_2015) * 100

sum_of_gross_income = sum(all_gross_income)

def robotext(sum_of_gross_income, largest_sale, pct_of_sales):
	format_numbers = lambda x: "{:,}".format(x)
	# sum_of_gross_income = "{:,}".format(sum_of_gross_income)
	sum_of_gross_income = format_numbers(sum_of_gross_income)
	largest_sale['GROSS_SALES'] = format_numbers(largest_sale['GROSS_SALES'])
	pct_of_sales = round(pct_of_sales)

	print """
	People are smoking the pot in Colorado.

	The state has earned a total ${} since legalizing marijuana in 2014.
	Sales boomed in {} {} when total sales reached ${}--{} percent of all sales that year.
	""".format(sum_of_gross_income, largest_sale['MONTH'].capitalize(), largest_sale['YEAR'], largest_sale['GROSS_SALES'], pct_of_sales)

robotext(sum_of_gross_income, largest_sale, pct_of_sales)


# wriite to different file format
with open('marijuana_gross_sales.json', 'wb') as outfile:
	json_data = json.dumps(data_dict, indent=4)
	outfile.write(json_data)

