# Make a Twilio account and fill information in here
# Options
phone_receive = '' # '+15557362'
phone_send = '' # '+15557362'
SID = ''
auth_token = ''
# /

# Imports
from twilio.rest import Client
#/

# Setup
client = Client(SID, auth_token)
# /

# Defs
def send_message(msg):
    message = client.messages.create(from_=phone_send, body=msg, to=phone_receive) 
# /
