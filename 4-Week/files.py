# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# Instructions:
# 1. Read a text file called "input.txt" and print its contents to the console.
# 2. Create a new file called "output.txt" and write the following modifications:
#    - Convert all text to uppercase.
#    - Replace all occurrences of the word "Python" with "JavaScript".
# 3. Print a message indicating that the modifications have been saved to "output.txt".
# 4. Handle any potential errors (e.g., file not found) gracefully.
# 5. Use functions to organize your code.
# 6. Include comments to explain your code.
# 7. Use exception handling to manage errors.
# 8. Use the 'with' statement for file operations to ensure proper resource management.
# 9. Use the os module to check if the input file exists before attempting to read it.
import os
import os
import sys
import sys
def read_file(file_path):
    """Reads the contents of a file and returns it."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)  # Exit the program with an error code

def write_file(file_path, content):
    """Writes the modified content to a new file."""
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Modifications have been saved to '{file_path}'.")
def modify_content(content):
    """Modifies the content by converting it to uppercase and replacing 'Python' with 'JavaScript'."""
    modified_content = content.upper()
    modified_content = modified_content.replace("PYTHON", "JAVASCRIPT")
    return modified_content
def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)  # Exit the program with an error code

    # Read the contents of the input file
    content = read_file(input_file)
    print("Original Content:")
    print(content)

    # Modify the content
    modified_content = modify_content(content)

    # Write the modified content to the output file
    write_file(output_file, modified_content)
if __name__ == "__main__":
    main()
# This program reads a file called "input.txt", modifies its content, and writes the modified content to "output.txt".