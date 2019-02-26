'''
To initialize the SMPT server enter the following command:
python -m smtpd -c DebuggingServer -n localhost:1025
'''

'''
Note: Gmail requires that you connect to port 465 if using
`SMTP_SSL()` and to port 587 when using `.starttls()`.
'''

# Imports
# ------------------------------------------------------
# Used to create SMTP connections
import email, smtplib, ssl
# Contain the HTML and plain-text versions of the email content
from email.mime.text import MIMEText
# Combine the HTML and plain-text versions into a single message
from email.mime.multipart import MIMEMultipart
# Used to encode attachments
from email import encoders
# Used to create attachments from files
from email.mime.base import MIMEBase
# Used for blind input
from getpass import getpass
# ------------------------------------------------------



# Start a secure SMTP connection
# ------------------------------------------------------

'''
Creates a secure connection with Gmail’s SMTP server, using the
`SMTP_SSL()` of `smtplib` to initiate a TLS-encrypted connection. 
The default context of ssl validates the host name and its 
certificates and optimizes the security of the connection. 
'''

def create_ssl_conn():
	# Port to connect to
	port = 465
	# Email account password
	password = getpass(prompt="Enter the email account password: ")

	# Create a secure SSL context
	context = ssl.create_default_context()

	# Initiate the TLS-encrypted connection
	# If `port`is 0 or unspecified, uses the default 465 port
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("z.devtest.costa@gmail.com", password)
		# Send email here

# ------------------------------------------------------



# Start an unsecure SMPT connection
# ------------------------------------------------------

'''
Instead of using `.SMTP_SSL()` to create a connection that is
secure from the start, we can create an unsecure SMTP connection
and encrypt it using `.starttls()`.
To do this, create an instance of `smtplib.SMTP`, which encapsulates
an SMTP connection and allows you access to its methods. 
'''

def create_startls_conn():
	smtp_server = "smtp.gmail.com"
	# Port to connect to with `.starttls()`
	port = 587
	sender_email = "z.devtest.costa@gmail.com"
	password = getpass(prompt="Enter the email account password: ")

	# Create a secure SSL context
	context = ssl.create_default_context()

	# Log in to the server and send emails (inside a `try` block)
	try:
		server = smtplib.SMTP(smtp_server, port)
		# Used to identify the script to the server
		# The hostname argument defaults to the fully qualified\
		# domain name of the local host.
		server.ehlo()
		# Make the connection secure
		server.starttls(context=context)
		server.ehlo()
		server.login(sender_email, password)
		# Send email here
	# If anything goes wrong, print the raised exception
	except Exception as e:
		print(e)
	# At the end, if everything went well, quit the server
	finally:
		server.quit()

# ------------------------------------------------------




# Send plain text emails
# ------------------------------------------------------

'''
After initiating a secure SMTP connection, using either of the
explained methods, you can send emails using `.sendmail()`
'''

# Port for SSL
def send_plain_text_ssl():
	port = 465
	smtp_server = "smtp.gmail.com"
	sender_email = "z.devtest.costa@gmail.com"
	receiver_email = "jose.fernando.costa.1998@gmail.com"
	password = getpass(prompt="Enter the email account password: ")
	# The string is formatted as such so that the email subject\
	# is correctly interpreted
	message = """\
	Subject: Test Email

	Test email sent using Python."""

	# Create a secure context
	context = ssl.create_default_context()
	# Initiate the TLS-encrypted connection
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		# Login into the sender account
		server.login(sender_email, password)
		# Send the email
		server.sendmail(sender_email, receiver_email, message)


# Sample code using `.startls()`

def send_plain_text_startls():
	# Port for `.startls()`
	port = 587
	smtp_server = "smtp.gmail.com"
	sender_email = "z.devtest.costa@gmail.com"
	receiver_email = "jose.fernando.costa.1998@gmail.com"
	password = getpass(prompt="Enter the email account password: ")
	message = """\
	Subject: Test Email

	Test email sent using Python."""

	# Create a secure context
	context = ssl.create_default_context()

	# Initiate the connection
	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()
		# Make the connection secure
		server.starttls(context=context)
		server.ehlo()
		# Login into the sender account
		server.login(sender_email, password)
		# Send the email
		server.sendmail(sender_email, receiver_email, message)

# ------------------------------------------------------



# Send HTML emails
# ------------------------------------------------------

'''
Today’s most common type of email is the MIME (Multipurpose
Internet Mail Extensions) Multipart email, combining HTML and
plain-text. 
MIME messages are handled by Python’s `email.mime` module.

Not all email clients display HTML content by default and some
people choose only to receive plain-text emails for security reasons.
Thus it is important to include a plain-text alternative for HTML messages.

The email client will render the last multipart attachment first, so add the
HTML message after the plain-text version.
'''

def send_html_email():
	sender_email = "z.devtest.costa@gmail.com"
	receiver_email = "jose.fernando.costa.1998@gmail.com"
	password = getpass(prompt="Enter the email account password: ")
	# Combines the contents into a single message
	message = MIMEMultipart("alternative")
	message["Subject"] = "Test Email Using MIME"
	message["From"] = sender_email
	message["To"] = receiver_email

	# Create the plain-text and HTML version of your message
	text = """\
	Hey, 
	Merry Christmas"""
	html = """\
	<html>
		<body>
			<h3>Hey</h3>
			<p>Merry Christmas</p>
			</body>
	</html>
	"""

	# Turn these into plain/html MIMEText objects
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)
	message.attach(part2)

	# Create a secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(
			sender_email, 
			receiver_email,
			message.as_string()
		)

# ------------------------------------------------------



# Send HTML emails with attachments
# ------------------------------------------------------

def send_html_email_attach():
	subject = "Test Email with Attachment"
	body = "Test email with attachment, created using Python."
	sender_email = "z.devtest.costa@gmail.com"
	receiver_email = "jose.fernando.costa.1998@gmail.com"
	password = getpass(prompt="Enter the email account password: ")

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	# Name of the attachment file
	attach_file = "fodder_file.txt"

	# Open the file in binary mode
	with open(attach_file, "rb") as attachment:
	    # Add file as application/octet-stream
	    # Email client can usually download this automatically as attachment
	    part = MIMEBase("application", "octet-stream")
	    part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
	    "Content-Disposition",
	    f"attachment; filename= {attach_file}",
	)

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)

# ------------------------------------------------------



# [Yagmail] Send an HTML email with attachments
# ------------------------------------------------------

import yagmail

def send_yagmail():
	receiver = "jose.fernando.costa.1998@gmail.com"
	body = "Email sent using Python and Yagmail."
	filename = "fodder_file.txt"

	yag = yagmail.SMTP("z.devtest.costa@gmail.com")
	yag.send(
		to=receiver,
		subject="Yagmail test with attachment",
		contents=body, 
		attachments=filename,
	)
# ------------------------------------------------------


if __name__ == "__main__":
	# send_plain_text_ssl()
	# send_plain_text_startls()
	# send_html_email()
	# send_html_email_attach()
	send_yagmail()


# Change keyring passwords for yagmail
# ------------------------------------------------------

'''
Note: to change a saved password with keyring, use the following code
import keyring
keyring.get_password('yagmail', '<email_account>')
keyring.set_password('yagmail', '<email_account>', '<new_password>')
keyring.get_password('yagmail', 'z.devtest.costa@gmail.com')
'''

# ------------------------------------------------------