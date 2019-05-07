"""
Problema da Calculadora:

Construa uma calculadora com as 4 operações básicas: soma, subtração, adicão, multiplição e divisão.

Faça 3 tipos de calculadora: uma em que o usuário inpute 2 números e depois o sinal da operação; outra que ele inpute o primeiro número, depois o sinal, depois o outro número e, por fim, a terceira em que o usuário inputa primeiro o sinal e depois os 2 numeros da operação.

>>> r = Calculadora(1,2)
>>> r.adicao()
3
>>> r.subtracao()
-1
>>> r.multiplicao()
2
>>> r.divisao()
0.5

"""

"""
>>> r= Calculadora



"""




class Calculadora:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def adicao(self):
        rsult = self.a + self.b
        return rsult

    def subtracao(self):
        rsult = self.a - self.b
        return rsult

    def multiplicao(self):
        rsult = self.a * self.b
        return rsult

    def divisao(self):
        rsult = self.a / self.b
        return rsult



