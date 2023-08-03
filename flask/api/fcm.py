# from pyfcm import FCMNotification
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
 
APIKEY = "424942461499"

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
# push_service = FCMNotification(APIKEY)
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)
def sendFCM(title='This is title',body='This is body',token=''):
    registration_token = token
    message = messaging.Message(
        notification = messaging.Notification(
            title=title,
            body=body
        ),
        token=registration_token,
    )

 
# def sendMessage(body, title, token):
#     # 메시지 (data 타입)
#     TOKEN = token
#     data_message = {
#         "body": body,
#         "title": title
#     }
 
#     # 토큰값을 이용해 1명에게 푸시알림을 전송함
#     result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
 
#     # 전송 결과 출력
#     print(result)
    
# sendMessage("SDsd","SDsd","Sdsdsdsd")
