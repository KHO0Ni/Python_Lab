def count_words_in_file(file_path):
    """
    Counts and displays the total number of words in a text file.

    Args:
        file_path (str): The path to the text file to be read.
    """
    try:
        # Try to open the file in read mode
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            # Split the content into words based on whitespace
            words = content.split()
            # Calculate the total number of words
            total_words = len(words)
            # Display the total number of words
            print(f"The total number of words in the file is: {total_words}")
    except FileNotFoundError:
        # This block will execute if the file does not exist
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        # This block will execute for any other exceptions
        print(f"An error occurred: {e}")

# This block ensures the code runs only if the script is executed directly
if __name__ == "__main__":
    # Define the path to the text file
    file_path = "D:\\verma\\2 Documents\\Anudip\\jupyter\\ABC.txt"
    # Call the function to count words in the file
    count_words_in_file(file_path)
    '''
    output:
    The total number of words in the file is: 12
    '''
