# Prompt user for file name
file_name = input("Enter a file name: ")

# Prompt user for personal information
name = input("Enter your name: ")
street_address = input("Enter your street address: ")
phone_number = input("Enter your phone number: ")

# Write personal information to file
with open(file_name, "w") as f:
    f.write(f"{name}, {street_address}, {phone_number}")

# Read and display contents of file
with open(file_name, "r") as f:
    contents = f.read()
    print("File contents:")
    print(contents)
#Note that this program assumes that the file name entered by the user is valid and can be written to and read from the current working directory. It also takes that the user enters their name, street address, and phone number in valid formats.