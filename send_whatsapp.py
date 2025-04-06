# pip install pywhatkit



# Ensure that you are logged into WhatsApp Web on your default browser before running the script.
# If your browser blocks pop-ups, the script may not work.



import pywhatkit as kit

# Phone number with country code, message, and time
phone_number = "+919434353611"  # Replace with the recipient's number
message = "Good night"
hour = 00  # 24-hour format
minute = 5


#kit.sendwhatmsg(phone_number, message, hour, minute)
# The sendwhatmsg() function requires a scheduled time,
# so hour and minute must be at least 1-2 minutes ahead of the current time.



try:
# If WhatsApp Web is not logged in, try-except block will prevent the script from crashing.
    
    kit.sendwhatmsg_instantly(phone_number, message)
# ends the message immediately without scheduling.
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
