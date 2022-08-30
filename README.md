# Amole pay integration

```python
import amole

amole = Amole(url="https://uatc.api.myamole.com:8076/amole/pay",
              signature='UkI_nVLwxKRHa1CSBAIRBJK-7hCB7mjc4mS5mCC3XXyvlnN4u9lc6HQRq52qNOaOiRv_7r5-8OVb79nh83eM',
              ip_address='196.188.54.245',
              username='eba',
              password='test')
response = amole.send_otp(card_number='+251910867889', merchant_id='SERDOTRAVEL')
print(response)

response = amole.pay(card_number='+251910867889', merchant_id='SERDOTRAVEL', amount='200', OTP='9999')
print(json.loads(response.content))
```