# Dictionary Password Cracker - Frank Grimmer 2023

import hashlib  # Import the hashlib library for hash functions.
import getpass  # Import getpass for secure password input (does not show user input).
import tkinter as tk  # Import tkinter library for creating GUI.
from tkinter import filedialog  # Import filedialog module from tkinter for the user to browse for file.

def select_wordlist():
    # Display intro messages.
    print("*** Dictionary Brute Force Password Cracker - Frank Grimmer 2023 ***")
    print("1. Select your own wordlist")
    print("2. Use the Ashley Madison wordlist (Default)")

    # Prompt user to choose a wordlist option.
    wordlist_option = input("Enter the number corresponding to your choice: ")

    # Checks the users choice.
    if wordlist_option == "1":
        # If the user chooses option 1, it will open a file dialog for them to select a wordlist file.
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        custom_wordlist = filedialog.askopenfilename(title="Select Wordlist File")
        root.destroy()  # Close the main window
        return custom_wordlist
    elif wordlist_option == "2":
        # If the user chooses option 2, set the default wordlist path.
        # Customize the path as needed.
        default_wordlist = ".\Ashley-Madison.txt"
        return default_wordlist
    else:
        # If the user enters an invalid option, display an error message and recursively call the function.
        print("Invalid option. Please enter 1 or 2.")
        return select_wordlist()

def display_loading():
    print("Calculating hash. Please wait...")


# Call the select_wordlist function and store the result in selected_wordlist.
selected_wordlist = select_wordlist()

# Prompt the user to enter a password without displaying it on the screen.
password = getpass.getpass("Please enter password: ")

# Encode the entered password to bytes using UTF-8 and calculate its MD5 hash.
enc_password = password.encode("UTF-8")
display_loading() # Displays a loading message for the user.
password_hash = hashlib.md5(enc_password.strip()).hexdigest()

# Open the selected wordlist file for reading.
wordlist = open(selected_wordlist, "r", encoding="utf-8")

# Iterate through each word in the wordlist file.
for word in wordlist:
    # Encode the current word to bytes using UTF-8 and calculate its MD5 hash.
    enc_word = word.encode("UTF-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()

    # Compare the hash of the entered password with the hash of the current word in the file.
    if password_hash == enc_hash:
        print("Password has been cracked. Password is: " + word)
        print("The password hash is: " + enc_hash)
        quit()

# If the loop completes without finding a match, indicate that the password was not in the wordlist.
print("Unable to crack password. Password is not in the wordlist.")
