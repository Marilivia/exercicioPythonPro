

"""
Problema da Calculadora:

Construa uma calculadora com as 4 operações básicas: soma, subtração, adicão, multiplição e divisão.

Faça 3 tipos de calculadora: uma em que o usuário inpute 2 números e depois o sinal da operação; outra que ele inpute o primeiro número, depois o sinal, depois o outro número e, por fim, a terceira em que o usuário inputa primeiro o sinal e depois os 2 numeros da operação.
class Calculadora:
    def __init__(self, x,s:str,y):
        self.a = x
        self.op = s
        self.b = y

    def operacao(self):
        if self.op == '+':
            rsult = self.a + self.b
            return rsult
        elif self.op == '-':
            rsult = self.a - self.b
            return rsult
        elif self.op == '*':
            rsult = rsult = self.a * self.b
            return rsult
        elif self.op == '/':
            rsult = self.a / self.b
            return rsult



>>> r = Calculadora(1,'+',2)
>>> r.operacao()
'1 + 2 = 3'
>>> r1 = Calculadora(1,'-',3)
>>> r1.operacao()
'1 - 3 = -2'
>>> r2 = Calculadora(2,'*',100)
>>> r2.operacao()
'2 * 100 = 200'
>>> r3 = Calculadora(2,'/',100)
>>> r3.operacao()
'2 / 100 = 0.02'

"""

"""
>>> r= Calculadora
"""


class Calculadora:
    def __init__(self, x,s:str,y):
        self.a = x
        self.op = s
        self.b = y

    def operacao(self):
        if self.op == '+':
            rsult = self.a + self.b
            return f'{self.a} {self.op} {self.b} = {rsult}'
        elif self.op == '-':
            rsult = self.a - self.b
            return f'{self.a} {self.op} {self.b} = {rsult}'
        elif self.op == '*':
            rsult = rsult = self.a * self.b
            return f'{self.a} {self.op} {self.b} = {rsult}'
        elif self.op == '/':
            rsult = self.a / self.b
            return f'{self.a} {self.op} {self.b} = {rsult}'









