def read_file_line_by_line(file_path):
    """
    Reads a text file line by line and displays the content.

    Args:
        file_path (str): The path to the text file to be read.
    """
    try:
        # Try to open the file in read mode ('r' means read mode)
        with open(file_path, 'r') as file:
            # Loop through each line in the file
            for line in file:
                # Print the current line without adding an extra new line
                print(line, end='')  # 'end=''' prevents adding an extra newline after each line
    except FileNotFoundError:
        # This block runs if the file does not exist
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        # This block runs for any other errors that occur
        print(f"An error occurred: {e}")

# This block makes sure the code below only runs if the script is executed directly
if __name__ == "__main__":
    # Define the path to the text file
    file_path = "D:\\verma\\2 Documents\\Anudip\\jupyter\\ABC.txt"
    # Call the function to read and print the file line by line
    read_file_line_by_line(file_path)

    '''
    Output:
    ABC.txt is this files name .

    this file contains content of ABC.txt.
    '''
