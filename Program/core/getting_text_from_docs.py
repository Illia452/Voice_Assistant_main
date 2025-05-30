from googleapiclient.discovery import build
from google.oauth2 import service_account
import time

class GetTextfromGoogleDocs():

    def __init__(self):

        SCOPES = ['https://www.googleapis.com/auth/documents']
        SERVICE_ACCOUNT_FILE = '../../rozpiznavanya/secret_data/gogAPI.json' 
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = build('docs', 'v1', credentials=creds)
        self.DOCUMENT_ID = '1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI'

    # витягуємо текст
    def extract_text(self, elements):
        text = ''
        for element in elements:
            if 'paragraph' in element:
                for run in element['paragraph']['elements']:
                    if 'textRun' in run:
                        text += run['textRun']['content']
        return text

    def print_text(self):
        start = time.time()
        doc = self.service.documents().get(documentId=self.DOCUMENT_ID).execute()
        content = doc.get('body').get('content')
        end_index = max(el.get('endIndex', 0) for el in content if 'endIndex' in el)

        text = self.extract_text(content)
        print(f"Оновлений текст:\n{text}")
        print(time.time()-start)
        time.sleep(0.5)

    def start(self):
        while True:
            self.print_text()



if __name__ == "__main__":
    get_text_docs = GetTextfromGoogleDocs()
    get_text_docs.start()

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