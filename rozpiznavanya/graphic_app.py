import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class VoiceAssistantGUI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Зображення зефірки
        zefir_image = Image(source='zefir.png')  # Замініть "zefir.png" на свій файл зображення
        layout.add_widget(zefir_image)

        # Індикатор "Активний"
        active_label = Label(text="Активний")
        layout.add_widget(active_label)

        # Кнопки керування
        button_layout = BoxLayout(orientation='horizontal')
        mic_button = Button(text="")
        button_layout.add_widget(mic_button)
        play_button = Button(text="▶")
        button_layout.add_widget(play_button)
        layout.add_widget(button_layout)

        # Текстове поле для введення команд
        command_entry = TextInput(hint_text="Введіть команду вручну...")
        layout.add_widget(command_entry)

        # Кнопка "Ввести команду вручну"
        enter_button = Button(text="Ввести команду вручну")
        layout.add_widget(enter_button)

        # Історія та налаштування
        bottom_layout = BoxLayout(orientation='horizontal')
        history_button = Button(text="Історія")
        bottom_layout.add_widget(history_button)
        settings_button = Button(text="Налаштування")
        bottom_layout.add_widget(settings_button)
        layout.add_widget(bottom_layout)

        return layout

if __name__ == '__main__':
    VoiceAssistantGUI().run()