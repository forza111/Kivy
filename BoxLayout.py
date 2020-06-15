from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical', #ориентация кнопок, по дефолту гор..
                       padding = [50,25,100,2],#отступ с каждой стороны
                       spacing = 100,) #отступы между виджетами
        bl.add_widget(Button(text='Кнопка1'))
        bl.add_widget(Button(text='Кнопка2'))
        bl.add_widget(Button(text='Кнопка3'))

        return bl




if __name__ == '__main__':
    BoxApp().run()