from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
# This uses Term Frequency Inverse Document Frequency, which essentially compares two text files for similarities of terms.
# This code compares all the emails against a single one right now. TODO: Add more emails.
def read_text_file(file_path):
    # Reads a file and returns the plain text of it.
    with open(file_path, 'r', encoding='utf-8') as file:

        text = file.read()
    return text

def compute_similarity(file1, file2):
    # Read text from files
    text1 = read_text_file(file1)
    text2 = read_text_file(file2)
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Compute TF-IDF vectors for the text
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # Compute cosine similarity between the TF-IDF vectors
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0,0]

    return similarity

def main():
    # main
    directory = 'CSC_424'
    email1_path = "Online Banking.txt"
    filenames = []
    scores = []
    for filename in os.scandir("spam_emails"):
        # Check if the files exist
        if not (os.path.exists(email1_path) and os.path.exists(filename)):
            print("Error: One or both email files do not exist.")
        else:
            # Compute similarity
            similarity = compute_similarity(email1_path, filename)

            # Print similarity
            filenames.append(filename)
            scores.append(similarity)
    
    for i in scores:
        # All the similarity scores
        if(i<.05):
            print(filenames[scores.index(i)],"Not Spam",i)
    # Least likely and most likely match.
    print(min(scores),max(scores))
    # A lower score is a perfect not-match. A score of 1 would be a perfect match.
    print(filenames[scores.index(min(scores))],filenames[scores.index(max(scores))])
main()
