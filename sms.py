import africastalking
import requests


class AfricasTalking:
    def __init__(self):
        self.username ="APP_USERNAME"
        self.api_key="API_KEY"
        africastalking.initialize(self.username, self.api_key)
        self.sms= africastalking.SMS
        
    #send sms
    def send_sms(self):
        recipients = ["+2547XXXXXXXX", "+2547XXXXXXXX"]
        message =  "Dear valued client, We regret to inform you that we are currently experiencing a fiber cut in our network.Our team is working hard to resolve the issue as quickly as possible and we expect to have the services restored soon."
        try:
            response=self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))
            
        
class StatusPage:
    def __init__(self):
        self.statuspage_api_key = "API_KEY"
        self.statuspage_page_id = "PAGE_ID"
        self.statuspage_url=f"https://api.statuspage.io/v1/pages/{self.statuspage_page_id}/incidents"
        self.headers={
            "Authorization": f"OAuth {self.statuspage_api_key}",
            "Content-Type": "application/json"
        }
        
    def create_incident(self):
        payload = {
            "incident": {
                "name": "Test Incident",
                "status": "Investigating",
                "body": {
                "markdown": "This is a test incident created by the Python script."
                }
            }
        }
        response = requests.post(self.statuspage_url, headers=self.headers, json=payload)
        return response.json()
    

client = AfricasTalking().send_sms()
print(client)