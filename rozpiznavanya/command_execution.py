import json
from list_commands import VoiceCommands
import time

class MakeCommands():
    def __init__(self):
        self.main_text = []
        self.voice_commands = VoiceCommands()
        self.output_data=[]
        with open('synonyms.json', 'r', encoding='utf-8') as f:
            self.output_data = json.load(f)
        self.history_data = []
        with open('history.json', 'r', encoding='utf-8') as f:
            self.history_data = json.load(f)
        self.list_ = []
        self.command = []
        self.list_command = []
        self.final_list_command = []
        self.history = []
        self.one_time = []
        self.indexx = False

    def remember_time(self, key_comm):
        loc_time = time.localtime()
        self.min = loc_time.tm_min
        self.hour = loc_time.tm_hour
        self.day = loc_time.tm_mday
        self.mon = loc_time.tm_mon
        self.year = loc_time.tm_year

        for key, vallue in self.history_data.items():
            self.history = vallue
        
        print(self.history_data)

        
        self.timmee = (f"{self.day}.{self.mon}.{self.year} - {self.hour}:{self.min}")
        self.one_time.append(key_comm)
        self.one_time.append(self.timmee)
        self.history.append(self.one_time)
        self.one_time = []
        print(self.history)

        self.history_data["history"] = self.history

        # Запис у файл
        with open('history.json', 'w', encoding='utf-8') as f:
            json.dump(self.history_data, f, ensure_ascii=False, indent=4)
        

    def text_from_App(self, text_from_edit):

        self.text_from_edit = text_from_edit
        self.indexx = True
        self.analyze_command(self.text_from_edit)
        

    def analyze_command(self, text):
        if self.indexx == True:
            text = [text]
            self.main_text = text
            self.indexx = False
        else:
            for i in text:
                self.main_text.append(' '.join(list(i)))

        # self.main_text = self.text_from_edit
        print(f"ОСТАННЯ ФРАЗА: {self.main_text}")

        for key, vallue in self.output_data.items():
            for val in vallue:
                for index, text_num in enumerate(self.main_text):
                    if val in text_num:
                        self.command.append(index)
                        self.command.append(key)
                        self.list_.append(self.command)

                        self.command = []


        
        for sen in self.list_:
            if sen not in self.list_command:
                self.list_command.append(sen)
        
        for _, command in self.list_command:
            if command not in self.final_list_command:
                self.final_list_command.append(command)
        print(" ")
        print("-------------------------------------")
        print(self.list_)
        print("-------------------------------------")
        print(self.list_command)
        print("-------------------------------------")
        print(self.final_list_command)
        print("-------------------------------------")

        
        
        for key_word in self.final_list_command:
            if key_word == "scrin":
                m_key = "Знімок екрану"
                self.voice_commands.TakeScreenShot()
                self.remember_time(m_key)

            elif key_word == "open_browser":
                m_key = "Відкриття браузера"
                self.voice_commands.OpenBrowser()
                self.remember_time(m_key)
        
                    
                    # elif key == "select_file" and (self.time_make_command_browze == 0.0 or time.time() - self.time_make_command_browze > 2):
                    #     self.voice_commands.SelectFile()
                    #     self.time_make_command_selectfile = time.time()
        self.main_text = []
        self.list_ = [] 
        self.list_command = []
        self.final_list_command = []
        