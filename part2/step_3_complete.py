# Import modules
import csv

# Write a function to do some exploring with strings
def working_with_strings(file_name):

    # Open the csv
    csv_file = open(file_name, 'rb')

    # Create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # Create a variable to represent the header row
    header_row = csv_data.next()

    # From the last lesson we know the variable header_row refers to a list.
    # Let's isolate the string that is 'GROSS SALES'
    print header_row

    # We'll do this by isolating in the list what is know as the index of the string
    print header_row[3]

    # Let's make sure this is a string
    print type(header_row[3])

    # Let's get the length of the string
    print len(header_row[3])

    # Create a variable to hold our string
    my_string = header_row[3]

    # Let's see how string subscripting works...
    # Let's print the third character
    print my_string[2]

    # Let's print the first five characters
    print my_string[:5]

    # Let's print everything after the first five characters
    print my_string[5:]

    # Let's capitalize the first letter in the string
    print my_string.capitalize()

    # Let's lowercase the string
    print my_string.lower()

    # Let's uppercase the string
    print my_string.upper()

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
working_with_strings('../data/marijuana_gross_sales.csv')