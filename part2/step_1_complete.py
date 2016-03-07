# Import modules
import csv

# Write a function that accepts one file name as an argument.
# The function should print each row from a csv file as well as each row's length and its type.
def output_rows_from(file_name):

	# Open the csv
	csv_file = open(file_name, 'rb')

	# Create the object that represents the data in the csv file
	csv_data = csv.reader(csv_file)

	# Loop through each row in the object
	for row in csv_data: 

		# Output the contents
		print row

		# Output the length of the row
		print len(row)

		# Output the type 
		print type(row)

	# Close the csv file
	csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
output_rows_from('../data/marijuana_gross_sales.csv')