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
