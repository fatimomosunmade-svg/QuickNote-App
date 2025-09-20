from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore  # For simple local data storage

# Define our screen layout using Kivy language syntax
KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1  # White background

        MDLabel:
            text: "QuickNote"
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 0, 0.4, 0.6, 1  # Nice blue color

        MDTextField:
            id: note_input
            hint_text: "Type your note here..."
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint: 0.8, 0.3
            multiline: True
            mode: "rectangle"
            max_text_length: 500

        MDRaisedButton:
            text: "SAVE NOTE"
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            size_hint: 0.6, 0.08
            on_release: app.save_note()
            md_bg_color: 0, 0.5, 0.7, 1  # Matching blue

        MDLabel:
            id: status_label
            text: ""
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            halign: "center"
            theme_text_color: "Secondary"
'''

class MainScreen(Screen):
    pass

class QuickNoteApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.store = JsonStore('notes.json')  # This file will store our notes
        return Builder.load_string(KV)

    def save_note(self):
        note_text = self.root.get_screen('main').ids.note_input.text
        if note_text.strip():  # Check if note is not empty
            try:
                # Save the note with a timestamp as the key
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.store.put(timestamp, text=note_text)
                self.root.get_screen('main').ids.status_label.text = f"Note saved at {timestamp}!"
                self.root.get_screen('main').ids.note_input.text = ""  # Clear the input
            except Exception as e:
                self.root.get_screen('main').ids.status_label.text = f"Error: {str(e)}"
        else:
            self.root.get_screen('main').ids.status_label.text = "Note is empty!"

if __name__ == '__main__':
    QuickNoteApp().run()
