import pywhatkit as kit

# Phone number (including country code) and message
phone_number = "+1"  # Replace with the recipient's phone number
message = "HI THERE!"

# Specify the time in 24-hour format (e.g., 16:30 for 4:30 PM)
hour = 16
minute = 25

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)
