import firebase_admin
from firebase_admin import credentials, storage

def firebaseDownload(filename='profile.jpg',bucket_id='bluegate-9ed94.appspot.com'): #path: 저장경로 #filename: 버켓에 있는 이미지 경로 #bucket_id: 사용할 버켓
    #Private key 

    cred = credentials.Certificate("./static/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {"storageBucket":bucket_id})
    
    bucket = storage.bucket()
    print(bucket)
    
    try:
        #버켓에 있는 이미지 불러옴
        blob = bucket.blob(filename)
        print(blob)
        #파일 저장
        blob.download_to_filename(f'./registedIMG/{filename}')
        
    #에러처리    
    except Exception as e:
        return str(e)
    
firebaseDownload()
    
        
