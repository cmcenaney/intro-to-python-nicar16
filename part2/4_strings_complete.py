# Import modules
import csv

# Write a function to do some more exploring with strings
def doing_more_with_strings(file_name):

    # Open the csv
    csv_file = open(file_name, 'rb')

    # Create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # Create a variable to represent the header row
    header_row = csv_data.next()

    # From the last lesson we know the variable header_row refers to a list.
    # Let's isolate the string that is 'GROSS_SALES'
    print header_row[3]

    # Create a variable to hold our string
    my_string = header_row[3]

    # Let's evaluate the uppercase version is equal to the lowercase version
    print my_string.upper() == my_string.lower()

    # Let's remove the underscore that is present in the string
    print my_string.replace('_', '')

    # Let's change the underscore to a space
    print my_string.replace('_', ' ')

    # Let's look at the strip method by giving it a value
    print my_string.strip('GROSS')

    # Let's try to split the string on the underscore
    print my_string.split('_')

    # Let's get the datatype for the thing we just created.
    # First let's create a variable to hold this string
    my_split_string = my_string.split('_')

    # Then let's get the type
    print type(my_split_string)

    # Because it's a list, we can again get a specfic item by it's index and we're back to where we started
    print my_split_string[0]

    # For the final item, let's use the length of the list and lowercase the two strings we created to create a sentence
    print 'The list is %d items long. We split it into two groups: %s and %s' % (len(my_split_string), my_split_string[0].lower(), my_split_string[1].lower())

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
doing_more_with_strings('../data/marijuana_gross_sales.csv')