source_file = input("Enter the name of the file to read: ")
destination_file = input("Enter the name of the file to create: ")

try:
    # Reading from source_file
    with open(source_file, 'r') as src:
        content = src.read()

    # Converting to uppercase
        content_modified = content.upper()

    # Write to destination_file
    with open(destination_file, 'w') as dest:
        dest.write(content_modified)

    print(f"Content from {source_file} has been read and written to {destination_file} in uppercase.")
except Exception as e:
    print(f"An error occurred: {e}")


except FileNotFoundError:
    print(f"Error: The file {source_file} was not found.")

except PermissionError:
    print(f"Error: You do not have permission to read/write {source_file}.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

while True:
    file1 = input("Enter the name of the first file: ")
    
    if file1.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        with open(file1, 'r') as f1:
            content1 = f1.read()
            print(f"Content of {file1}:\n{content1}")
    except FileNotFoundError:
        print(f"Error: The file {file1} was not found.")
    
    except PermissionError:
        print(f"Error: You do not have permission to read {file1}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
