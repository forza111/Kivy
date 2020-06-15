from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class GridApp(App):
    def build(self):
        gl = GridLayout(cols=10,rows=10,#нужно указать сols или rows,или то и то
                        padding = [30],
                        spacing = 3)

        for x in range(55):
            gl.add_widget(Button(text = 'X'))


        return gl




if __name__ == '__main__':
    GridApp().run()