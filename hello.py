from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        label = Label(text = "Hello Kivy",font_size = "60sp",italic = True,
        color = "blue",bold = True)

        return label
    
MyApp().run()