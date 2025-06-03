from googleapiclient.discovery import build
from google.oauth2 import service_account
import time
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot

class GetTextfromGoogleDocs(QObject):

    close_push = pyqtSignal()

    def __init__(self, control_signals):
        super().__init__()
        SCOPES = ['https://www.googleapis.com/auth/documents']
        SERVICE_ACCOUNT_FILE = '../../rozpiznavanya/secret_data/gogAPI.json' 
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = build('docs', 'v1', credentials=creds)
        self.DOCUMENT_ID = '1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI'
        self.control_signals = control_signals
        self.push_running = False
        self.isText = False

        self.get_text_running = True

        control_signals.start_writeText.connect(self.status_Push_ON)
        control_signals.stop_writeText.connect(self.status_Push_OFF)

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

    
    def clear_text(self):
        if len(self.text) == 1:
            return
        else:
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

    def stop_GetText(self):
        self.get_text_running = False


    def start(self):
        self.print_text()
        self.clear_text()
        while True:
            if self.push_running:
                self.print_text()
                self.wait_text()
            if self.get_text_running == False:
                break
    
    def wait_text(self):
        if self.isText:
            self.control_signals.transfer_text_toPush(self.text)

    def chech_whether_isText(self):
        if len(self.text) > 1:
            self.isText = True

    @pyqtSlot()
    def status_Push_ON(self):
        self.push_running = True

    @pyqtSlot()
    def status_Push_OFF(self):
        self.push_running = False

if __name__ == "__main__":
    get_text_docs = GetTextfromGoogleDocs()
    get_text_docs.start()

