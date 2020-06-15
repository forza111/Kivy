from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics','resizable',0) #нельзя менять размер окна
Config.set('graphics','width',400)
Config.set('graphics','height',500)


class CalculatorApp(App):
    def update_label(self):
        self.lbl.text=self.formula

    def add_number(self,instance):
        if (self.formula == '0'):
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self,instance):
        if(str(instance.text).lower() == 'x'):
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self,instance):
        self.lbl.text = str(eval(self.lbl.text)) #eval позволяет вычислять**
        self.formula = '0'


    def build(self):

        self.formula = '0'

        gl = GridLayout(cols = 4,
                        spacing = 3,#отступы между виджетами
                        size_hint = (1,.6)) #ширина 100, высота 60 процентов
        bl = BoxLayout(orientation = 'vertical',
                       padding = 25) #отступ с каждой стороны



        self.lbl = Label(text = '0',#Виджет Label для отображения текста
                            font_size = 40, #размер шрифта
                            size_hint = (1,.4),
                            valign = 'center', #bottom, middle,center,top указывает горизонтально выравнивание
                            halign = 'right', #лево центр и право,указывает вертикальное выравнивание
                            text_size = (400-50,500*.4-50))#задает ширины и высоту для текстуры текста
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text = '7',on_press = self.add_number))
        gl.add_widget(Button(text = '8',on_press = self.add_number))
        gl.add_widget(Button(text = '9',on_press = self.add_number))
        gl.add_widget(Button(text = 'x',on_press = self.add_operation))

        gl.add_widget(Button(text = '4',on_press = self.add_number))
        gl.add_widget(Button(text = '5',on_press = self.add_number))
        gl.add_widget(Button(text = '6',on_press = self.add_number))
        gl.add_widget(Button(text = '-',on_press = self.add_operation))

        gl.add_widget(Button(text = '1',on_press = self.add_number))
        gl.add_widget(Button(text = '2',on_press = self.add_number))
        gl.add_widget(Button(text = '3',on_press = self.add_number))
        gl.add_widget(Button(text = '+',on_press = self.add_operation))

        gl.add_widget(Widget()) #создает пустой виджет
        gl.add_widget(Button(text = '0',on_press = self.add_number))
        gl.add_widget(Button(text = '.',on_press = self.add_operation))
        gl.add_widget(Button(text = '=',on_press = self.calc_result))

        bl.add_widget(gl)
        return bl

if __name__ == '__main__':
    CalculatorApp().run()