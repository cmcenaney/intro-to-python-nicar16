"""
First, we'll import several standard library modules to use. These are some of the most frequently used libaries
in Python. Also, these three double quotes--you can use single quotes too--create a multi-line string. It's great
For adding a large comment like this one or for setting a variable to a large block of text.
"""
import os
import csv
import json


# Use the os module to select file name
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

# get all gross values from list using list comprehension 
all_gross_sales = [d[3] for d in data]

# sum(all_gross_sales)  # this will fail

# create a list to dict function using def
def list_to_dict(alist):
	# alist vs list
	return dict( zip(header_row, alist) )

# create a list to dict function using lambda
list_to_dict = lambda alist: dict( zip(header_row, alist) )

# convert data to a list of dictionaries instead a list of lists (sometimes called two dimensional array/list)
data_dict = [list_to_dict(d) for d in data]

# clean up the data to use types that work for analysis
for d in data_dict:
	# make all gross sales floats
	d['GROSS_SALES'] = float(d['GROSS_SALES'])
	# remove white space from month
	d['MONTH'] = d['MONTH'].strip()

# get all gross values from list using list comprehension and new dictionary format
all_gross_sales = [d['GROSS_SALES'] for d in data_dict]  # reads better!

# get the average gross sale values over two years
average_gross_sales =  sum(all_gross_sales) / len(all_gross_sales)

# filter for 2015
data_2015 = [d for d in data_dict if d['YEAR'] == '2015']

# filter for 2015 gross sales
all_gross_sales_2015 = [d['GROSS_SALES'] for d in data_2015]

# get the average gross sales for 2015
average_gross_sales_2015 = sum(all_gross_sales_2015) / len(all_gross_sales_2015)

# get the dictionary based on the largest gross sale
largest_sale = max(data_dict, key=lambda x:float(x['GROSS_SALES']))

# get the dictionary based on the smallest gross sale
smallest_sale = min(data_dict, key=lambda x:float(x['GROSS_SALES']))

# Get the what percent of total sales largest_sale 
pct_of_sales = largest_sale['GROSS_SALES'] / sum(all_gross_sales_2015) * 100

# ge the sum
sum_of_gross_sales = sum(all_gross_sales)

# generate robo text
def robotext(sum_of_gross_sales, largest_sale, pct_of_sales):
	# create lambda function to format numbers
	format_numbers = lambda x: "{:,}".format(x)
	# sum_of_gross_sales = "{:,}".format(sum_of_gross_sales)
	# format sum_of_gross_sales
	sum_of_gross_sales = format_numbers(sum_of_gross_sales)
	# format largest_sale['GROSS_SALES']
	largest_sale['GROSS_SALES'] = format_numbers(largest_sale['GROSS_SALES'])
	# round pct to keep it simple
	pct_of_sales = round(pct_of_sales)

	# generate robotext
	print """
	People are smoking the pot in Colorado.

	The state has earned a total ${} since legalizing marijuana in 2014.
	Sales boomed in {} {} when total sales reached ${}--{} percent of all sales that year.
	""".format(sum_of_gross_sales, largest_sale['MONTH'].capitalize(), largest_sale['YEAR'], largest_sale['GROSS_SALES'], pct_of_sales)

# execute robo text
robotext(sum_of_gross_sales, largest_sale, pct_of_sales)


# use with to open marijuana_gross_sales.json file
with open('marijuana_gross_sales.json', 'wb') as outfile:
	# convert list of dictionaries to JSON and add indentation for easy reading
	json_data = json.dumps(data_dict, indent=4)
	# write to file system
	outfile.write(json_data)

