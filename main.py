# Description: This file reads the contents of a file and prints the number of words in the document and the frequency of each letter in the document

#Importing the necessary libraries
import sys
import os

#Main function
def main():

    #Checking if the number of arguments is correct
    if len(sys.argv) != 2:

        #Printing the usage of the file if the number of arguments is incorrect
        print ("Usage: python main.py <path_to_file>")
        sys.exit(1)

    #Reading the path to the file
    path_to_file = sys.argv[1]
    file_reader(path_to_file)

def file_reader (path_to_file):

    #Reading Contents of the file
    with open (path_to_file) as f:
        contents = f.read ()

        file_name = os.path.basename(path_to_file)
        print (f"--- Begin report of {file_name} ---\n")

        #Counting the number of words in the document
        words = contents.split ()
        print (len(words), "words found in the document\n")

        #Making a dictionary of the letters and their frequency
        letter_dict = {}
        for i in contents.lower():
            if i in letter_dict and i.isalpha():
                letter_dict[i] += 1
            elif i.isalpha():
                letter_dict[i] = 1

        #Printing the frequency of each letter
        for key, value in sorted(letter_dict.items(), key=lambda item: item[1], reverse=True):
            print ("The", "'"+key+"'", "character was found", value, "times")

#Calling the main function
main()