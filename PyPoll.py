# The data we need to retrieve/
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# Add our dependencies.
import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:
    


# To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
 

# # Close the file.
# election_data.close()



# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")

# Use the with statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#outfile.write("Hello World")
    # txt_file.write("Counties in the Election\n-------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()



