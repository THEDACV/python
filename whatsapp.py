import pywhatkit
phone_number=input('enter a number with a country code:')
message=input('enter your message:')
pywhatkit.sendwhatmsg_instantly(phone_number,message,tab_close=True)

