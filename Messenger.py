import os

# Create a variable called name and assign your name to it
name = "Steve"

# Ask the user for a messenger file name
file_name = input("Enter the messenger file name: ")

# Add .txt if the user did not include it
if not file_name.endswith(".txt"):
    file_name = file_name + ".txt"

# Check if the file already exists
if os.path.exists(file_name):
    # Open and read the existing file
    with open(file_name, "r") as file:
        contents = file.read()

    print("\nCurrent messages:")
    print(contents)

else:
    # Create the file if it does not exist
    with open(file_name, "w") as file:
        pass

    print("New messenger file created:", file_name)

# Ask the user to enter a message
message = input("Enter your message: ")

# Add the name to the beginning of the message
message = "[" + name + "]: " + message

# Add the message to the file
with open(file_name, "a") as file:
    file.write(message + "\n")

print("Message saved to", file_name)