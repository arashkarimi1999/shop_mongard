from kavenegar import *
from os import getenv


def send_otp_code(phone_number, code):
    try:
        print("code:", code)
        api = KavenegarAPI(getenv('KAVENEGAR_API'))
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تائید شما {code}'
        }
        response = api.sms_send(params)

    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
