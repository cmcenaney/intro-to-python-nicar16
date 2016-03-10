# Import modules
import csv

# Write a function to output the first row of a csv file and get the column names
def output_first_csv_row(file_name):

    # Open the csv
    csv_file = open(file_name, 'rb')

    # Create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # Create a variable to represent the header row
    header_row = csv_data.next()

    # Output the value
    print header_row

    # Uutput the length of the header row
    print len(header_row)

    # Output the type of the header row
    print type(header_row)

    # Loop through each item in the header_row
    for column_name in header_row:

        # Output its contents
        print column_name

        # Output its length
        print len(column_name)

        # Output its type
        print type(column_name)

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
output_first_csv_row('../data/marijuana_gross_sales.csv')