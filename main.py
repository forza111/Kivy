from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers.html import HtmlLexer
from kivy.config import Config

Config.set('graphics','resizable','0'); #нельзя менять размер окна
Config.set('graphics','width','640'); #ширина окна
Config.set('graphics','height','480'); #высота окна

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class MyApp(App):
    def build(self):

           s = Scatter()
           fl = FloatLayout(size = (300,300))
           s.add_widget(fl) #Scatter позволяет  менять двумя пальцами размер кнопки и вращать ее
           fl.add_widget(Button(
               text='ETO MOIA first knopka',
               font_size=16, #размер шрифта
               on_press = self.btn_press,
               background_color = [1,0,0,1], #цвет кнопки
               background_normal = '',#для более насыщенного цвета
               size_hint = (.5,.25), #ширина кнопки 50 процентов окна, высота25
               pos = (640/2-160 ,480/2-60))); #координаты расположения кнопки по х и у
           return s

    def btn_press(self, instance):
        print('Кнопка нажата') #Печатает в консоли "КНопка нажата"
        instance.text = 'Я нажата'  #после нажатия текст сменится на "я нажата"

if __name__ == '__main__':
    MyApp().run()