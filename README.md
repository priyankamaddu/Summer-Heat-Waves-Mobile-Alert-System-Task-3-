
# 🌞 Summer Heatwave Alert System with SMS Notifications

This project detects heatwaves based on historical temperature data and sends precautionary SMS alerts via the Twilio API to help people stay safe during extreme temperatures.

## Features
- Detects heatwaves based on temperature thresholds and consecutive hot days.
- Customizable temperature threshold and consecutive days for detecting heatwaves.
- Provides appropriate precautions based on the average temperature.
- Sends SMS notifications using Twilio API to inform users about upcoming heatwaves and necessary precautions.

## Requirements
- Python 3.x
- Libraries:
  - `pandas`
  - `twilio`
  - `streamlit`

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/summer-heatwave-alert-system.git
cd summer-heatwave-alert-system
```

### 2. Install dependencies:
```bash
pip install pandas twilio streamlit
```

### 3. Twilio Setup:
- Create an account on [Twilio](https://www.twilio.com/).
- Get your **Account SID** and **Auth Token** from your Twilio dashboard.
- Purchase a Twilio phone number from which the alerts will be sent.

### 4. Update the code:
- In the `send_sms()` function, replace `'YOUR_ACCOUNT_SID'` and `'YOUR_AUTH_TOKEN'` with your actual Twilio credentials.
- Update the `from_='NUMBER'` in the same function with your Twilio phone number.

### 5. Add the CSV file:
- Place your historical temperature data CSV file at the specified path (default: `'D:\Summer Heat Wave Alert\historical_temperature_data.csv'`).
- Make sure your CSV file has a column for temperature data (`'Data.Temperature.Avg Temp'`) and dates (`'Date.Full'`).

### 6. Run the app:
```bash
streamlit run app.py
```

## Usage
1. Open the app in your browser using the link provided by Streamlit.
2. Enter the desired phone number to receive SMS alerts.
3. Adjust the temperature threshold and the number of consecutive days to define a heatwave.
4. Review the heatwave detection results displayed on the app.
5. Click "Send SMS Notifications" to send precautionary messages to the phone number provided.

## CSV File Format
The CSV file should have at least two columns:
- **Date.Full**: A date column (e.g., `'2024-09-24'`)
- **Data.Temperature.Avg Temp**: The average temperature in °C for that date.

Example:

| Date.Full  | Data.Temperature.Avg Temp |
|------------|---------------------------|
| 2024-09-21 | 35.2                      |
| 2024-09-22 | 34.8                      |
