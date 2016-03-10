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
    

    # Create a variable to hold our string
    

    # Let's evaluate the uppercase version is equal to the lowercase version
    

    # Let's remove the underscore that is present in the string
    

    # Let's change the underscore to a space
    

    # Let's look at the strip method by giving it a value
    

    # Let's try to split the string on the underscore
    

    # Let's get the datatype for the thing we just created.
    # First let's create a variable to hold this string
    

    # Then let's get the type
    

    # Because it's a list, we can again get a specfic item by it's index and we're back to where we started
    

    # For the final item, let's use the length of the list and lowercase the two strings we created to create a sentence
    

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
doing_more_with_strings('../data/marijuana_gross_sales.csv')