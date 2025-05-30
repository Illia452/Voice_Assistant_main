from googleapiclient.discovery import build
from google.oauth2 import service_account
import time


# підключаємо json із ключами
SCOPES = ['https://www.googleapis.com/auth/documents']
SERVICE_ACCOUNT_FILE = '../../rozpiznavanya/secret_data/gogAPI.json' 

# cтворюємо об'єкт автентифікації
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=creds)

# id документа (можна взяти з url Google Docs)
DOCUMENT_ID = '1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI'



# отримуємо вміст документа
doc = service.documents().get(documentId=DOCUMENT_ID).execute()
content = doc.get('body').get('content')

# витягуємо текст
def extract_text(elements):
    text = ''
    for element in elements:
        if 'paragraph' in element:
            for run in element['paragraph']['elements']:
                if 'textRun' in run:
                    text += run['textRun']['content']
    return text

end_index = doc.get('body').get('content')[-1]['endIndex']

while True:
    start = time.time()
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()
    content = doc.get('body').get('content')
    text = extract_text(content)
    print("\nОновлений текст:\n", text)
    print(time.time()-start)
    time.sleep(0.5)



# requests = [
#     {
#         'deleteContentRange': {
#             'range': {
#                 'startIndex': 1,
#                 'endIndex': end_index - 1
#             }

#         }

#     },
# ]
# result = service.documents().batchUpdate(
#     documentId=DOCUMENT_ID, body={'requests': requests}).execute()