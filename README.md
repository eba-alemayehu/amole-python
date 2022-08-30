# Amole pay integration

This python library is to help you integrate with amole api. Contact amole team for integration.
```python
import amole
import json, requests

amole = Amole(url="https://uatc.api.myamole.com:8076/amole/pay",
              signature='<SEGNITURE>',
              ip_address='<YOUR IP>',
              username='<USERNAME>',
              password='<TEST>')
response = amole.send_otp(card_number='<CARD OR PHONENUMBER>', merchant_id='<MERCHANT ID>')
print(response)

response = amole.pay(card_number='<CARD OR PHONENUMBER>', merchant_id='<MERCHANT ID>', amount='200', OTP='9999')
print(json.loads(response.content))
```