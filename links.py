import ssl
import socket
import re
import email
import os
def extract_links_from_email(email_content):
    # Scans the text from the email and saves any links in an array.
    msg = email.message_from_string(email_content)
    links = []

    for part in msg.walk():
        # For each part of the email, this regex finds any urls.
        if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
            links.extend(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', part.get_payload()))

    return links

def check_certificate(domain):
    # If a link is found, try connecting to it. If for some reason
    # The connection fails, it's most likely spam.
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
    # Reads the email, finds the results of the links, and returns a boolean.   
    links = extract_links_from_email(email_content)

    for link in links:
        domain = re.search(r'https?://([^/]+)', link).group(1)

        if not check_certificate(domain):
            return True

    return False

# Example usage
def main(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        email_content = file.read()
    return is_spam(email_content)

