# Import modules
import csv

# Write a function to do some exploring with numbers
def exploring_with_numbers(file_name):

    # Open the csv
    csv_file = open(file_name, 'rb')

    # Create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # Create a variable to represent the header row
    header_row = csv_data.next()

    # Let's get the first row of data
    data_row = csv_data.next()

    # Let's create a variable off the bat to isolate the number that is the gross sales
    my_number = data_row[3]

    # Let's output the value
    print my_number

    # Let's get the length of the number
    print len(my_number)

    # For kicks, let's multiply gross sales by 2.
    # We should get 36567671.24, assuming the gross sales we're using is 18283835.62.
    # Because it's not an number, when we try to double it, python will simply repeat the string.
    print my_number * 2

    # Let's double-check its type
    print type(my_number)

    # Let's convert the string to a number 
    my_number = float(my_number)
    print my_number


    # Now let's try some math...

    # Multiplication
    print my_number * 2

    # Division
    print my_number / 2

    # Addition
    print my_number + 1000

    # Subtraction
    print my_number - 1000

    # Order of operations
    print (my_number * 2 + 56) / 100

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
exploring_with_numbers('../data/marijuana_gross_sales.csv')
