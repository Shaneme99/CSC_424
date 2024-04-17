#The program is supposed return True if is not spam, and False if it is spam.
#Spam is determined by reading all of the words from the input txt file and comparing them to the scam_word_list.txt file for matches.


def read_words_from_file(file_path): # This function reads words from a text file and returns them as a list
    try:
        with open(file_path, 'r') as file:
            words = file.read().split() # Read the entire contents of the file and split it into words
        return words
    except FileNotFoundError:
        print(f"File '{file_path}' not found.") # If the file is not found, print an error message and return an empty list

        return []


def check_for_scams(sample_words, scam_words): # This function checks if any word from the sample list matches the scam word list
    for word in sample_words: # Iterate over each word in the sample list
        if word.lower() in scam_words: # If the lowercase version of the word is found in the scam word set, return False
            return False # If no matching word is found, return True
    return True



def main(): # Define file paths for the sample file and the scam word list
    sample_file_path = r"spam_emails/1712254363.6939_3.txt"
    scam_word_list_path = r"scam_word_list.txt"

    sample_words = read_words_from_file(sample_file_path)     # Read words from both files
    scam_words = set(read_words_from_file(scam_word_list_path)) # Convert scam word list into a set for efficient membership testing


    if sample_words and scam_words: # If both lists are not empty, check for scams
        result = check_for_scams(sample_words, scam_words)
        print(result)   # Print the result (True if no scam word found, False otherwise)

    else:
        print("Unable to check for scams.") # If either of the files is empty, print an error message


if __name__ == "__main__": # Entry point of the program
    main()
