from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyCalc(GridLayout):

    def __init__(self, **kwargs):
        super(MyCalc, self).__init__(**kwargs)
        self.rows = 5

        self.panel = TextInput()
        self.add_widget(self.panel)

        box = BoxLayout()
        self.btnSeven = Button(text='7',on_press=self.sete)
        self.btnEight = Button(text='8',on_press=self.oito)
        self.btnNine = Button(text='9',on_press=self.nove)
        self.btnMenos = Button(text='-',on_press=self.subtracao)
        box.add_widget(self.btnSeven)
        box.add_widget(self.btnEight)
        box.add_widget(self.btnNine)
        box.add_widget(self.btnMenos)
        self.add_widget(box)

        box2 = BoxLayout()
        self.btnFour = Button(text='4',on_press=self.quatro)
        self.btnFive = Button(text='5',on_press=self.cinco)
        self.btnSix = Button(text='6',on_press=self.seis)
        self.btnSoma = Button(text='+',on_press=self.adicao)
        box2.add_widget(self.btnFour)
        box2.add_widget(self.btnFive)
        box2.add_widget(self.btnSix)
        box2.add_widget(self.btnSoma)
        self.add_widget(box2)

        box3 = BoxLayout()
        self.btnOne = Button(text='1',on_press=self.um)
        self.btnTwo = Button(text='2',on_press=self.dois)
        self.btnThree = Button(text='3',on_press=self.tres)
        self.btnVezes = Button(text='*',on_press=self.multiplicacao)
        box3.add_widget(self.btnOne)
        box3.add_widget(self.btnTwo)
        box3.add_widget(self.btnThree)
        box3.add_widget(self.btnVezes)
        self.add_widget(box3)

        box4 = BoxLayout()
        self.btnAC = Button(text='AC',on_press=self.limpar)
        self.btnZero = Button(text='0',on_press=self.zero)
        self.btnEqual = Button(text='=',on_press=self.exibir)
        self.btnDivisor = Button(text='/',on_press=self.divisao)
        box4.add_widget(self.btnAC)
        box4.add_widget(self.btnZero)
        box4.add_widget(self.btnEqual)
        box4.add_widget(self.btnDivisor)
        self.add_widget(box4)


    def exibir(self,button):
        self.decide()

    def limpar(self,button):
        self.panel.text = ''

    def subtracao(self, button):
        self.panel.text += ' - '

    def adicao(self, button):
        self.panel.text += ' + '

    def multiplicacao(self, button):
        self.panel.text += ' * '

    def divisao(self, button):
        self.panel.text += ' / '

    def zero(self, button):
        self.panel.text += '0'

    def um(self, button):
        self.panel.text += '1'

    def dois(self, button):
        self.panel.text += '2'

    def tres(self, button):
        self.panel.text += '3'

    def quatro(self,button):
        self.panel.text += '4'

    def cinco(self,button):
        self.panel.text += '5'

    def seis(self,button):
        self.panel.text += '6'

    def sete(self, button):
        self.panel.text += '7'

    def oito(self, button):
        self.panel.text += '8'

    def nove(self, button):
        self.panel.text += '9'

    def decide(self):
        numero = eval(self.panel.text)
        print(str(numero))
        self.panel.text = str(numero)


class MyApp(App):
    def build(self):
        return MyCalc()

MyApp().run()














'''
self.num1 = TextInput(multiline=True)
self.add_widget(self.num1)

self.l2 = Label(text="Digite outro numero: ")
self.add_widget(self.l2)

self.num2 = TextInput(multiline=True)
self.add_widget(self.num2)

self.somar = Button(text="Efetuar soma", font_size=40)
self.somar.bind(on_press=self.pressionar)
self.add_widget(self.somar)

self.l2 = Label(text="O resultado é: ")
self.add_widget(self.l2)

self.resultado = TextInput(multiline=True)
self.add_widget(self.resultado)

def pressionar(self, instance):
self.resultado.text = str(int(self.num1.text) + int(self.num2.text))
'''