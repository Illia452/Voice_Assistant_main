from googleapiclient.discovery import build
from google.oauth2 import service_account
import time
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot

class GetTextfromGoogleDocs(QObject):

    close_push = pyqtSignal()

    def __init__(self, work_with_text):
        super().__init__()
        SCOPES = ['https://www.googleapis.com/auth/documents']
        SERVICE_ACCOUNT_FILE = '../../rozpiznavanya/secret_data/gogAPI.json' 
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = build('docs', 'v1', credentials=creds)
        self.DOCUMENT_ID = '1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI'
        self.work_WithText = work_with_text

        self.time_open_push = 0

        self.get_text_running = True

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
        doc = self.service.documents().get(documentId=self.DOCUMENT_ID).execute()
        content = doc.get('body').get('content')
        self.end_index = max(el.get('endIndex', 0) for el in content if 'endIndex' in el)

        self.text = self.extract_text(content)
        time.sleep(0.5)

        self.set_text()

    def stop_GetText(self):
        self.get_text_running = False


    def set_text(self):
        if self.work_WithText.pushIS_Active:
            self.work_WithText.receive_google_docs_text(self.text)
            self.wait_speech()

    def wait_speech(self):
        self.time_open_push = time.time()
        print(f"ЦЕ ДОВЖИНА НАШОГО ТЕКСТУ: {len(self.text)}")
        if time.time() - self.time_open_push >= 4.8 and len(self.text) == 1:
            self.work_WithText.pushIS_Active = False
            self.close_push.emit()
            print("СИГНАЛ ЩО ПУШ ЗАКРИВАЄМО")
            


    def start(self):
        self.print_text()
        
        while True:
            self.print_text()
            if self.get_text_running == False:
                break

    
    def clear_text(self):
        requests = [
            {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': self.end_index - 1
                    }

                }

            },
        ]
        result = self.service.documents().batchUpdate(
            documentId=self.DOCUMENT_ID, body={'requests': requests}).execute()


    

if __name__ == "__main__":
    get_text_docs = GetTextfromGoogleDocs()
    get_text_docs.start()

