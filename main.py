# import fundamentals libs
import requests
import os
from twilio.rest import Client
from functions import transfor_data, generate_message

# Retrieve the weather API key, SID,TOKEN and numbers from the environment variables
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
PERSONAL_NUMBER = os.environ.get('PERSONAL_NUMBER')

# End point
WEATHER_URL = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q=CULIACAN&days=1&aqi=no&alerts=no'

# --------------- FUNCTIONS -------------------
def send_ws(payload):
    """
    Send a WhatsApp message using Twilio API.

    Args:
        payload (str): The message payload to be sent.

    Returns:
        None
    """
    # Initialize Twilio client
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    
    # Create and send the WhatsApp message
    message = client.messages.create(
        from_=f'whatsapp:{TWILIO_NUMBER}',  
        body=payload,                       
        to=f'whatsapp:{PERSONAL_NUMBER}')
#------------------------------------------------


# Get the data
response = requests.get(url=WEATHER_URL)

# Retrieve the first item from the 'forecastday' list and access the 'hour' object
hour_forecast = response.json()['forecast']['forecastday'][0]['hour']

# extract the data of interest and transform it into a pandas DataFrame
clean_forecast = transfor_data(hour_forecast)

# Generate the experiment schedule message based on the provided clean forecast data
message = generate_message(clean_forecast)

send_ws(message)

