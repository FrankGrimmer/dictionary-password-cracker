# Dictionary Brute Force Password Cracker

## Overview

This Python-based password-cracking tool is designed to perform a dictionary attack using a wordlist. Users can either choose their own custom wordlist or use the default Ashley Madison wordlist.

## Features

- User-friendly menu for wordlist selection.
- Secure password input using the `getpass` library.
- MD5 hash generation for entered passwords and wordlist words.
- Comparison of hashed passwords for password cracking.

## Usage

1. Run the script: `python cracker.py`
2. Follow the on-screen instructions to select a wordlist option and enter a password.
3. The program will calculate the MD5 hash of the entered password and compare it with the hashes in the selected wordlist.
4. If a match is found, the cracked password is displayed.

## Options

- Option 1: Select your own wordlist.
- Option 2: Use the default Ashley Madison wordlist (hardcoded path).

## Requirements

- Python 3.x
- tkinter library (for selecting a custom wordlist)

## How to Run

1. Ensure you have Python installed.
2. Run the script in your terminal or command prompt: `python cracker.py`

## Note

- The default Ashley Madison wordlist is hardcoded in the script. Please change file path as needed.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The project uses the hashlib library for hash functions.
