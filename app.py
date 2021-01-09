from twilio.rest import Client
import urllib.request as urllib2
import json

READ_API_KEY='81PI7L29I5RGQVSR'
CHANNEL_ID="1263897"
conn = urllib2.urlopen("http://api.thingspeak.com/channels/{}/feeds/last.json?api_key={}".format(CHANNEL_ID,READ_API_KEY))

response = conn.read()
print("http status code={}".format(conn.getcode()))
data=json.loads(response)
data['field1'],data['created_at']
conn.close()

if float(data['field1']) > 25.0:
    account_sid = 'AC5b16f250693ba61a46319701f4cc2d68' 
    auth_token = 'cc54777eebad87f831e84199a63fc4e6' 
    client = Client(account_sid, auth_token) 
     
    message = client.messages.create( 
                                  from_='+12517326281',  
                                  body='Temperature: - '+ data['field1'] + ' recorded at ' + data['created_at'],      
                                  to='+918778796951' 
                              ) 
     
    print(message.sid)
