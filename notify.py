# Imports
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

def create_message(customer_info, food_, order_id, order_total):

    wallet = customer_info['wallet']
    first_name = customer_info['first_name']
    last_name = customer_info['last_name']
    name = f"{first_name} {last_name}"
    email = customer_info['email']

    # Create the base text message.
    msg = EmailMessage()
    msg['Subject'] = "SnackCoin Rewards Test Order"
    msg['From'] = Address("SnackCoin Rewards", "snackcoin", "test.com")
    msg['To'] = Address(
        f"{first_name} {last_name}",
        first_name,
        email
    )
    msg.set_content(f"""\
    Hello {name}!

    You placed an order: #{order_id}
    
    The total was {order_total}

    This is a test email
    """)

    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.

    msg.add_alternative("""\
    <html>
    <head></head>
    <body>
        <h1>Hello!</h1>
        <p>This is a test email</p>
    </body>
    </html>
    """, subtype='html')

    return msg

def send_email(msg):
    # Send the message via local SMTP server.
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)
