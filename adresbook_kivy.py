from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from adresbook import AdressBook


Config.set('graphics','resizable',0) #нельзя менять размер окна
Config.set('graphics','width',400)
Config.set('graphics','height',500)


class AdresBookApp(App):
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

        '''gl = GridLayout(cols = 4,
                        spacing = 3,#отступы между виджетами
                        size_hint = (1,.6)) #ширина 100, высота 60 процентов'''

        bl = BoxLayout(orientation = 'vertical',
                       padding = 25,#отступ с каждой стороны
                       spacing = 1,
                       size_hint = (1,.6))



        self.lbl = Label(text = '0',#Виджет Label для отображения текста
                            font_size = 40, #размер шрифта
                            size_hint = (1,.4),
                            valign = 'top', #bottom, middle,center,top указывает горизонтальное выравнивание
                            halign = 'left', #лево центр и право,указывает вертикальное выравнивание
                            text_size = (400-50,500*.4-50))#задает ширины и высоту для текстуры текста
        bl.add_widget(self.lbl)

        bl.add_widget(Button(text = 'Поиск контакта',on_press = self.add_number))
        bl.add_widget(Button(text = 'Добавить контакт',on_press = self.add_number))
        bl.add_widget(Button(text = 'Изменить контакт',on_press = self.add_number))
        bl.add_widget(Button(text = 'Посмотреть информацию о контакте',on_press = self.add_operation))
        bl.add_widget(Button(text = 'Удалить контакт',on_press = self.add_operation))


        '''bl.add_widget(gl)'''
        return bl

if __name__ == '__main__':
    AdresBookApp().run()