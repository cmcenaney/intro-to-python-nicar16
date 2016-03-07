# Import modules
import csv

# Write a function to do some exploring with integers
def working_with_integers(file_name):

    # Open the csv
    csv_file = open(file_name, 'rb')

    # Create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # Create a variable to represent the header row
    header_row = csv_data.next()

    # Let's get the first row of data
    data_row = csv_data.next()

    # Let's create a variable off the bat to isolate the integer that is the gross sales
    my_integer = data_row[3]

    # Let's output the value
    print my_integer

    # Let's get the length of the integer
    print len(my_integer)

    # For kicks, let's multiply gross sales by 2.
    # We should get 36567671.24, assuming the gross sales we're using is 18283835.62.
    # Because it's not an integer, when we try to double it, python will simply repeat the string.
    print my_integer * 2

    # Let's double-check its type
    print type(my_integer)

    # Let's convert the string to an integer
    my_integer = float(my_integer)
    print type(my_integer)

    # Now let's try some math...

    # Multiplication
    print my_integer * 2

    # Division
    print my_integer / 2

    # Addition
    print my_integer + 1000

    # Subtraction
    print my_integer - 1000

    # Order of operations
    print (my_integer*2+56)/100

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
working_with_integers('../data/marijuana_gross_sales.csv')