
# installed twilio using pip install twilio for sending message locally from machine

from twilio.rest import Client 
 
account_sid = '(authId)' 
auth_token = '(auth_token)' 
client = Client(account_sid, auth_token) 

def send_msg():
	
 
            message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='hiiiiiiiiiii',      
                                  to='whatsapp:+91(mobileNumber)' 
                               ) 
 
            print(message.sid)


#installed advanced python scheduler for scheduling message using pip install apscheduler