# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)


def send_twilio_message(message: str, sender_id: str) -> None:
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=sender_id
    )
    print(message.sid)
    return None

def send_twilio_photo(message: str, sender_id: str, media_url: str) -> None:
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=sender_id,
        media_url=media_url
    )
    print(message.sid)
    return None
