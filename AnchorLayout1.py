from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class AnchorApp(App):
    def build(self):
        al = AnchorLayout(anchor_x = 'left',anchor_y = 'top')
        #опционально можно добавить расположение кнопки,по умолчанию по центру

        al.add_widget(Button(text = 'BATONIII',
                             size_hint = [.52,.52]))
        #размеры кнопки в процентах от доступного размера
        #если указать size = [*,*] то значения будут фиксированные


        return al

if __name__ == '__main__':
    AnchorApp().run()