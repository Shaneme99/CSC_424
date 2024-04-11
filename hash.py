import hashlib

def main(email):
    sample_hash = get_hash("sample.txt")
    email_text = read_text(email)
    email_hash = get_hash(email_text)
    sample_hash
    print(email_hash)

def read_text(file_path):
    try:
        with open(file_path, 'r') as file:
            full_text = "".join(file.readlines())
            md5_hash = hashlib.md5(full_text.encode())
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return

def get_hash(email):
    sha256_hash = hashlib.sha256(email.encode())
    return sha256_hash.hexdigest()

# Example usage:
file_path = input("input the name of the email to check without .txt")+".txt"
main(file_path)
