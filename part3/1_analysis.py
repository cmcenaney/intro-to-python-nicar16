import os
import csv
import json

file_name = "marijuana_gross_sales.csv"
file_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data', file_name))

# Open the csv
csv_file = open(file_path, 'rb')

# Create the object that represents the data in the csv file
csv_data = csv.reader(csv_file)

# Create a variable to represent the header row
header_row = csv_data.next()  # explain generators

data = list(csv_data)

all_gross_income = [d[3] for d in data]  # this will fail

# sum(all_gross_income)  # error

all_gross_income = [float(d[3]) for d in data]
average_gross_income =  sum(all_gross_income) / len(all_gross_income)

data_2015 = [d for d in data if d[0] == '2015']
all_gross_income_2015 = [float(d[3]) for d in data_2015]
average_gross_income_2015 = sum(all_gross_income_2015) / len(all_gross_income_2015)

# data_2014 = [d for d in data if d[0] == '2014']
# all_gross_income_2014 = [float(d[3]) for d in data_2014]
# average_gross_income_2014 = sum(all_gross_income_2014) / len(all_gross_income_2014)

# def turn_value_to_float(value):
# 	return float(value)

# lambda value:float(value)

largest_sale = max(data, key=lambda x:float(x[3]))
smallest_sale = min(data, key=lambda x:float(x[3]))

pct_of_sales = float(largest_sale[3]) / sum(all_gross_income_2015) * 100

def list_to_dict(alist):
	# alist vs list
	return dict( zip(header_row, alist) )

list_to_dict = lambda alist: dict( zip(header_row, alist) )

data_dict = [list_to_dict(d) for d in data]

with open('marijuana_gross_sales.json', 'wb') as outfile:
	json_data = json.dumps(data_dict)
	outfile.write(json_data)

