from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
#from kivy.uix.scrollview import ScrollView
#from kivy.uix.label import Label
# from kivy.uix.button import Button 

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)  #vincular os eventos de teclado com o método bind
    
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)  #desvincular os eventos de teclado com o método unbind

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test (App):
    def build(self):
        return Gerenciador()

Test().run()



        # box = BoxLayout(orientation="vertical")
        # button = Button(text="click", font_size=30, on_release=self.incrementar)
        # self.label = Label(text="1", font_size=30)
        # box.add_widget(button)
        # box.add_widget(self.label)

        # box2 = BoxLayout()
        # button2 = Button(text="Botão de alguma coisa 2")
        # label2 = Label(text="Label disso aqui 2")
        # box2.add_widget(button2)
        # box2.add_widget(label2)
        #box.add_widget(box2)

    # def incrementar(self, button):
    #     #button.text = 'to solto'
    #     self.label.text = str(int(self.label.text) + 1)





