from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.properties import DictProperty

Config.set('graphics', 'width', str('603'))
Config.set('graphics', 'height', str('600'))

class Home(BoxLayout):
	vez = 1
	vencedor = 0
	jogadas = 0

	def selecionado(self, bt):
		if bt.text == '':
			if self.vez == 1:
				bt.text = 'X'
				self.vez = 2
			elif self.vez == 2:
				bt.text = 'O'
				self.vez = 1
			self.verificarFim()
		elif bt.text != '' and self.jogadas != 9 and self.vencedor == 0:
			self.ids.info.text = 'Já foi jogado'			

	def casasIguais(self, a, b, c):
		for n in range(1,10,1):
			if a == n:
				btA = self.ids[f"bt{n}"]
				conteudoA = btA.text
			elif b == n:
				btB = self.ids[f"bt{n}"]
				conteudoB = btB.text
			elif c == n:
				btC = self.ids[f"bt{n}"]
				conteudoC = btC.text
		if ((conteudoA == conteudoB) and (conteudoB == conteudoC) and (conteudoA != None and conteudoA != "")):
			if self.vez == 2 and self.vencedor == 0:
				self.vencedor = 1
			else:
				self.vencedor = 2
			return True
		else:
			return False
	
	def verificarFim(self):
		if (self.casasIguais(1, 2, 3) or self.casasIguais(4, 5, 6) 
			or self.casasIguais(7, 8, 9) or self.casasIguais(1, 4, 7)
			or self.casasIguais(2, 5, 8) or self.casasIguais(3, 6, 9)
			or self.casasIguais(1, 5, 9) or self.casasIguais(3, 5, 7)):
			self.ids.info.text = f"O vencedor é: {self.vencedor}"
		else:
			self.ids.info.text = f"Vez do jogador {self.vez}!!!"
			self.jogadas += 1
		if self.jogadas == 9:
			self.ids.info.text = f"Deu velha!!!"
			
	def novo(self, bt):
		self.ids.bt1.text = ''
		self.ids.bt2.text = ''
		self.ids.bt3.text = ''
		self.ids.bt4.text = ''
		self.ids.bt5.text = ''
		self.ids.bt6.text = ''
		self.ids.bt7.text = ''
		self.ids.bt8.text = ''
		self.ids.bt9.text = ''
		self.ids.info.text = 'Jogador %d começa' % self.vez
		self.vencedor = 0
		self.jogadas = 0
		for n in range(1,10,1):
			self.ids[f"bt{n}"].text = ''
				
root = Builder.load_string('''
#:set tam_font dp('80')

<Botao@Button>:
	font_size: tam_font

Home:
	orientation: 'vertical'
	padding: dp('5')
	spacing: dp('5')
	BoxLayout:
		size_hint: 1, .2
		Label:
			id: info
			text: 'Jogador %d começa' % root.vez
			font_size: sp('20')
		Button:
			text: 'Novo'
			size_hint_x: .2
			on_release:
				root.novo(self)
	GridLayout:
		rows: 3
		cols: 3
		#spacing: dp('5')
		#padding: dp('5')
		Botao:
			id: bt1
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt2
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt3
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt4
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt5
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt6
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt7
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt8
			text: ''
			on_press:
				root.selecionado(self)
		Botao:
			id: bt9
			text: ''
			on_press:
				root.selecionado(self)
''')

runTouchApp(root)
