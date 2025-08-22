source_file = input("Enter the name of the file to read: ")
destination_file = input("Enter the name of the file to create: ")

try:
    # read
    with open(source_file, 'r') as src:
        content = src.read()

    # Convert to uppercase
        content_modified = content.upper()

    # Write to destination_file
    with open(destination_file, 'w') as dest:
        dest.write(content_modified)

    print(f"Content from {source_file} has been read and written to {destination_file} in uppercase.")
except Exception as e:
    print(f"An error occurred: {e}")
