import hash
import links
import scan_words
import os
for filename in os.listdir('spam_emails'):
    filename = "spam_emails/"+filename
    test1 = scan_words.main(filename) # True if spam
    test2 = links.main(filename) # True if spam
    test3 = hash.main(filename) # True if spam
    if(test1 or test2 or test3):
        print(filename + " is spam!")
    else:
        print(filename + " is NOT spam!")
    print('---------------------')