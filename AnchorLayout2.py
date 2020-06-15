from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class AnchorApp(App):
    def build(self):


        al = AnchorLayout()

        bl = BoxLayout(orientation = 'vertical',size_hint = [.4,.4]) #размеры кнопок

        bl.add_widget(TextInput()) #TextInput позволяет вводить текст
        bl.add_widget(TextInput())
        bl.add_widget(Button(text = 'Войти'))


        al.add_widget(bl)#помещаем в переменную bl - al
        return al




if __name__ == '__main__':
    AnchorApp().run()