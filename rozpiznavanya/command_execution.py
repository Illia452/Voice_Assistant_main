import json
from list_commands import VoiceCommands

class MakeCommands():
    def __init__(self):
        self.main_text = []
        self.voice_commands = VoiceCommands()
        self.output_data=[]
        with open('synonyms.json', 'r', encoding='utf-8') as f:
            self.output_data = json.load(f)
        self.list_com = []
        self.com = []

    def analyze_command(self, text):
        for i in text:
            self.main_text.append(' '.join(list(i)))

        print(f"ОСТАННЯ ФРАЗА: {self.main_text}")

        for key, vallue in self.output_data.items():
            for values in vallue:
                if values in self.main_text[0]:
                    print(f"НАША КОМАНДА {values} з ключа {key}")
                    if key == "scrin":
                        self.voice_commands.TakeScreenShot()
                    elif key == "open_browser":
                        self.voice_commands.OpenBrowser()
                    
                    
                    # elif key == "select_file" and (self.time_make_command_browze == 0.0 or time.time() - self.time_make_command_browze > 2):
                    #     self.voice_commands.SelectFile()
                    #     self.time_make_command_selectfile = time.time()
        self.main_text = []