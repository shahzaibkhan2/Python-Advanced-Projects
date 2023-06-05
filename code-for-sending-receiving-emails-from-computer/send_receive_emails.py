# In order to use emails we use python module and smt,imaplib module
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create the email message
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = recipient_email
    email['Subject'] = subject
    email.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email)

    print("Email sent successfully.")

# Function to receive emails
def receive_emails(email, password):
    # Connect to the IMAP server
    with imaplib.IMAP4_SSL('imap.gmail.com') as server:
        server.login(email, password)
        server.select("INBOX")
        _, data = server.search(None, "ALL")
        email_ids = data[0].split()

        for email_id in email_ids:
            _, email_data = server.fetch(email_id, "(RFC822)")
            raw_email = email_data[0][1]
            print(raw_email)  # Print the raw email content

# Example usage
sender_email = "myname_email@gmail.com"
sender_password = "12345678"
recipient_email = "another_email@yahoo.com"
subject = "Hello from Shahzaib!"
message = "This is the body of the email."

send_email(sender_email, sender_password, recipient_email, subject, message)
receive_emails(sender_email, sender_password)
