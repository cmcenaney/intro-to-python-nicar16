# Import modules
import csv

# Write a function to do some exploring with numbers
def working_with_numbers(file_name):

    # Open the csv
    csv_file = open(file_name, 'rb')

    # Create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # Create a variable to represent the header row
    header_row = csv_data.next()

    # Let's get the first row of data
    

    # Let's create a variable off the bat to isolate the number that is the gross sales
    

    # Let's output the value
    

    # Let's get the length of the number
    

    # For kicks, let's multiply gross sales by 2.
    # We should get 36567671.24, assuming the gross sales we're using is 18283835.62.
    # Because it's not a number, when we try to double it, python will simply repeat the string.
    

    # Let's double-check its type
    

    # Let's convert the string to a floating point number
   
    

    # Now let's try some math...

    # Multiplication
    

    # Division
    

    # Addition
    

    # Subtraction
    


    # Let's see how if statements work when dealing with a csv file
    # Loop through all rows in the data
    

        # Print the whole row if the year is 2014
        
            

        # Print the whole row if the year is 2014 and the month is May
        # Otherwise, print just the gross sales
        
            
        
            

    # Close the csv file when we're done
    csv_file.close()

# Call the function, passing as an argument the name of the csv file to open.
working_with_numbers('../data/marijuana_gross_sales.csv')


