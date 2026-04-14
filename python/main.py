"""Per-call prompt personalization with dynamic variable substitution."""

import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

from patter import Patter

phone = Patter(
    mode="local",
    openai_key=os.getenv("OPENAI_API_KEY"),
    twilio_sid=os.getenv("TWILIO_ACCOUNT_SID"),
    twilio_token=os.getenv("TWILIO_AUTH_TOKEN"),
    phone_number=os.getenv("TWILIO_PHONE_NUMBER"),
    webhook_url=os.getenv("WEBHOOK_URL"),
)

agent = phone.agent(
    system_prompt=(
        "You are a scheduling assistant for Acme Health. "
        "You are speaking with {customer_name} (account {account_number}). "
        "Their next appointment is on {appointment_date}. "
        "Help them reschedule, confirm, or cancel."
    ),
    voice="nova",
    first_message="Hi {customer_name}! I see your appointment on {appointment_date}. How can I help?",
    variables={
        "customer_name": "Jane Doe",
        "account_number": "AC-12345",
        "appointment_date": "March 20th",
    },
)

CUSTOMER_DB = {
    "+14155551234": {
        "customer_name": "Alice Chen",
        "account_number": "AC-78901",
        "appointment_date": "April 3rd",
    },
    "+14155555678": {
        "customer_name": "Bob Martinez",
        "account_number": "AC-45678",
        "appointment_date": "April 10th",
    },
}


async def on_call_start(data):
    caller = data.get("caller", "")
    customer = CUSTOMER_DB.get(caller)
    if customer:
        print(f"Known caller {caller} -> {customer['customer_name']}")
        return {"variables": customer}
    print(f"Unknown caller {caller} — using defaults")
    return None


if __name__ == "__main__":
    asyncio.run(phone.serve(agent, port=8000, on_call_start=on_call_start))
