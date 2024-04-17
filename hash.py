from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
# This uses Term Frequency Inverse Document Frequency, which essentially compares two text files for similarities of terms.
# The program scans an email and compares it to the target email, a banking notice that I pulled from my personal email.
# As a result, this program doesn't do well with base64 encoded emails.
# The difference between the emails is assigned a score from 0 to 1. The higher, the more different.
# Higher scores are associated with a higher likilehood of being spam.
# This code compares all the emails against a single one right now.
def read_text_file(file_path):
    # Reads a file and returns the plain text of it.
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def compute_similarity(file1, file2):
    # Get strings from files.
    text1 = read_text_file(file1)
    text2 = read_text_file(file2)
    
    # Create TF-IDF vectorizer, program to find difference between emails.
    vectorizer = TfidfVectorizer()

    # Compute TF-IDF vectors for the text. Generates each vector.
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # Compute cosine similarity between the TF-IDF vectors, bound between 0 and 1.
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0,0]

    return similarity

def main(filename):
    # main
    email1_path = "Online Banking.txt"
    # Compute similarity
    similarity = compute_similarity(email1_path, filename)
    if similarity < .2:
        return False
    else:
        return True
