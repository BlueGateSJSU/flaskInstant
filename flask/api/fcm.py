# from pyfcm import FCMNotification
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
# push_service = FCMNotification(APIKEY)
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)
def sendFCM(title='여기는 유민이라 알리고 통신상태 양호한지',body='Im min',token=''):
    registration_token = token
    message = messaging.Message(
        notification = messaging.Notification(
            title=title,
            body=body
        ),
        token=registration_token,
    )
    response = messaging.send(message)
    print(response)
sendFCM(token='cuoJ1qAlTIOZaWcBuCh6Ig:APA91bHGDQVzmtyb9MYiaPJn0569iFU5VwUmL6oxYM64eazDKW45heRTBzz07xjuqZgHtO2muLAWmlgI75sd_T8-CfSiBF697urkE3rD4LAxVLEMPAo753PtVcOi_CqBeZAPjoauwNnY')

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
