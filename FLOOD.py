from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics','width',1300)
Config.set('graphics','height',400)

class CalcApp(App):
    def build(self):
        gl = GridLayout(cols = 12,rows = 2, spacing = 0.5,size_hint=(1,.9))
        bl = BoxLayout(orientation = 'vertical')

        self.lbl = Label(text = 'o',font_size = 40,size_hint = (1,.5),valign = 'top',halign = 'left',
                         text_size=(1300,400*.5-50))

        self.formula = '0'

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='1'))
        gl.add_widget(Button(text='2'))
        gl.add_widget(Button(text='3'))
        gl.add_widget(Button(text='4'))
        gl.add_widget(Button(text='5'))
        gl.add_widget(Button(text='6'))
        gl.add_widget(Button(text='7'))
        gl.add_widget(Button(text='8'))
        gl.add_widget(Button(text='9'))
        gl.add_widget(Button(text='0'))
        gl.add_widget(Button(text='-'))
        gl.add_widget(Button(text='+'))

        gl.add_widget(Button(text='q'))
        gl.add_widget(Button(text='w'))
        gl.add_widget(Button(text='e'))
        gl.add_widget(Button(text='r'))
        gl.add_widget(Button(text='t'))
        gl.add_widget(Button(text='y'))
        gl.add_widget(Button(text='u'))
        gl.add_widget(Button(text='i'))
        gl.add_widget(Button(text='o'))
        gl.add_widget(Button(text='p'))
        gl.add_widget(Button(text='['))
        gl.add_widget(Button(text=']'))

        bl.add_widget(gl)
        return bl

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self,instance):
        self.formula += str(instance.text)





if __name__ == '__main__':
    CalcApp().run()
