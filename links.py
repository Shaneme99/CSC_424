import ssl
import socket
import re
import email
import os
def extract_links_from_email(email_content):
    msg = email.message_from_string(email_content)
    links = []

    for part in msg.walk():
        if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
            links.extend(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', part.get_payload()))

    return links

def check_certificate(domain):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()

            # Check if the certificate is valid
            if cert:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error checking certificate for {domain}: {e}")
        return False

def is_spam(email_content):
    links = extract_links_from_email(email_content)

    for link in links:
        domain = re.search(r'https?://([^/]+)', link).group(1)

        if not check_certificate(domain):
            return True

    return False

# Example usage
if __name__ == "__main__":
    for filename in os.scandir("spam_emails"):
        with open(filename, 'r', encoding='utf-8') as file:
            email_content = file.read()
        if is_spam(email_content):
            print("The email is spam!")
        else:
            print("The email is not spam.")
