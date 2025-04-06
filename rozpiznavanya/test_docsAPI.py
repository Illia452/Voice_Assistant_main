from googleapiclient.discovery import build
from google.oauth2 import service_account
import time


# Підключаємо JSON-файл із ключами
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = 'gogAPI.json'  # Вкажи правильний шлях

# Створюємо об'єкт автентифікації
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Створюємо сервісний об'єкт API
service = build('docs', 'v1', credentials=creds)

# Вкажи ID документа (можна взяти з URL Google Docs)
DOCUMENT_ID = '1BSSH9i6B4XgVx-KHpXiV2BTgZJ7_KL-U7QpklqugGoQ'



# Отримуємо вміст документа
doc = service.documents().get(documentId=DOCUMENT_ID).execute()
content = doc.get('body').get('content')

# Витягуємо текст
def extract_text(elements):
    text = ''
    for elem in elements:
        if 'paragraph' in elem:
            for run in elem['paragraph']['elements']:
                if 'textRun' in run:
                    text += run['textRun']['content']
    return text



while True:
    start = time.time()
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()
    content = doc.get('body').get('content')
    text = extract_text(content)
    print("\nОновлений текст:\n", text)
    print(time.time()-start)
    time.sleep(0.5)

