import json
import urllib.parse

import requests


class Amole:
    def __init__(self,
                 url,
                 signature,
                 ip_address,
                 username,
                 password):
        self.url = url
        self.signature = signature
        self.ip_address = ip_address
        self.username = username
        self.password = password

    def send_reqeust(self,
                     card_number,
                     merchant_id,
                     payment_action,
                     OTP='',
                     amount='',
                     expiration_date='',
                     description='',
                     source_transaction_id='',
                     vendor_account='',
                     additional_info_1='',
                     additional_info_2='',
                     additional_info_3='',
                     additional_info_4=''):
        payload = {
            'BODY_CardNumber': card_number,
            'BODY_ExpirationDate': expiration_date,
            'BODY_PaymentAction': payment_action,
            'BODY_AmountX': amount,
            'BODY_PIN': OTP,
            'BODY_AmoleMerchantID': merchant_id,
            'BODY_OrderDescription': description,
            'BODY_SourceTransID': source_transaction_id,
            'BODY_VendorAccount': vendor_account,
            'BODY_AdditionalInfo1': additional_info_1,
            'BODY_AdditionalInfo2': additional_info_2,
            'BODY_AdditionalInfo3': additional_info_3,
            'BODY_AdditionalInfo4': additional_info_4
        }

        headers = {
            'HDR_Signature': self.signature,
            'HDR_IPAddress': self.ip_address,
            'HDR_UserName': self.username,
            'HDR_Password': self.password,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", self.url, headers=headers, data=urllib.parse.urlencode(payload),
                                    verify=False)
        return response

    def send_otp(self, **kwargs):
        return self.send_reqeust(payment_action='09', **kwargs)

    def pay(self, OTP, **kwargs):
        return self.send_reqeust(payment_action='01', OTP=OTP, **kwargs)


