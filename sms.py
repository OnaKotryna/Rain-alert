from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


def send_sms(text):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.getenv("FROM_NUMBER"),
        body=text,
        to=os.getenv("TO_NUMBER")
    )

    # print(message.sid)