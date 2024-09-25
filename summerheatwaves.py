import pandas as pd
from twilio.rest import Client
import streamlit as st

# Path to your CSV file
CSV_FILE_PATH = 'D:\Summer Heat Wave Alert\historical_temperature_data.csv'  # Update this to your CSV file path

def detect_heatwaves(data, threshold=30, consecutive_days=3):
    data['heatwave'] = False
    count = 0

    for i in range(len(data)):
        if data['Data.Temperature.Avg Temp'].iloc[i] > threshold:
            count += 1
        else:
            count = 0

        if count >= consecutive_days:
            data.loc[i, 'heatwave'] = True

    return data

def get_precautions(avg_temp):
    """Return precautions based on the average temperature."""
    if 25 <= avg_temp <= 28:
        return "Stay hydrated and wear light clothing."
    elif 29 <= avg_temp <= 32:
        return "Limit outdoor activities and take breaks in the shade."
    elif avg_temp > 32:
        return "Avoid strenuous activities and stay indoors during peak hours."
    else:
        return "Temperature is normal, no special precautions needed."

def send_sms(to, message):
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='NUMBER',
        to=to
    )

    st.success(f"Message sent to {to}: {message.sid}")

# Streamlit app
st.title('Heatwave Detection and SMS Notification')

# Load data from the specified CSV file
data = pd.read_csv(CSV_FILE_PATH)

# Input for phone number
phone_number = st.text_input('Enter phone number to send SMS')

# Inputs for threshold and consecutive days
threshold = st.number_input('Temperature Threshold (°C)', value=30)
consecutive_days = st.number_input('Consecutive Days for Heatwave', value=3)

# Apply heatwave detection
data = detect_heatwaves(data, threshold, consecutive_days)

# Display data
st.write(data)

# Button to send SMS
if st.button("Send SMS Notifications"):
    if phone_number:
        for index, row in data.iterrows():
            if row['heatwave']:
                avg_temp = row['Data.Temperature.Avg Temp']
                precautions = get_precautions(avg_temp)
                message = (f"🌞 Heatwave detected on {row['Date.Full']}! "
                            f"Average temperature: {avg_temp}°C. "
                            f"Precautions: {precautions}")
                send_sms(phone_number, message)
    else:
        st.error("Please enter a valid phone number.")
