# https://changhsinlee.com/pyderpuffgirls-ep4/
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from pathlib import Path

def send_email(username, password, recipient, subject, body, attachment=None):
    """Send email via Gmail

    :param username: Gmail username that is also used in the "From" field
        e.g. pyderpuffgirls@gmail.com
    :param password: Gmail password
    :param recipient: a string or list of the email address of recipient(s)
    :param subject: the subject of email
    :param body: the body of email
    :param attachment: a string or list of the path(s) of the file(s) to attach, default: None
    """

    smtp_server = "smtp.gmail.com"
    port = 465
    ssl_context = ssl.create_default_context()

    # https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
    if isinstance(recipient, str):
        recipient = [recipient]
    recipients_string = ', '.join(recipient)  # e.g. "person1@gmail.com, person2@gmail.com"

    # create email
    email = MIMEMultipart()

    # Add body, then set the email metadata
    if body is not None:
        content = MIMEText(body)
        email.attach(content)

    email['Subject'] = subject
    email['From'] = username
    email['To'] = recipients_string

    if attachment is not None:
        _add_attachments(email, attachment)

    with smtplib.SMTP_SSL(smtp_server, port, context=ssl_context) as conn:

        conn.login(username, password)
        conn.sendmail(username, recipient, email.as_string())
        print(f'Sent email to {recipients_string}')

    pass


def _add_attachments(mime_part: MIMEMultipart, file_paths):
    """
    Add attachment to the email object from file paths
    """

    if isinstance(file_paths, str):
        file_paths = [file_paths]

    for file_path in file_paths:
        file_name = Path(file_path).name

        with open(file_path, 'rb') as file:
            part = MIMEApplication(file.read())

        part.add_header('Content-Disposition', f'attachment; filename={file_name}')
        mime_part.attach(part)

    return mime_part

if __name__ == '__main__':
    from os.path import join, dirname
    from dotenv import load_dotenv
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    gmail_username = os.environ['GMAIL_USERNAME']
    gmail_password = os.environ['GMAIL_PASSWORD']

    send_email(
        username=gmail_username,
        password=gmail_password,
        recipient='wahe3b@gmail.com',
        subject='This is a test with an attachment',
        body='this is a  test with an attachment \nCarry on...',
        attachment=['README.md', 'notes.txt']
    )
