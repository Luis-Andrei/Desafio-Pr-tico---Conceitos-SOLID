'''
OPEN CLOSED PRINCIPLE

Solução refatorada seguindo o Princípio Aberto-Fechado.
Cada tipo de exame implementa sua própria lógica de aprovação através de uma interface comum.
'''

from abc import ABC, abstractmethod

class Exame(ABC):
    @abstractmethod
    def verificar_condicoes(self):
        pass

class ExameSangue(Exame):
    def __init__(self):
        self.tipo = "sangue"

    def verificar_condicoes(self):
        # Implementação específica para exame de sangue
        return True  # Exemplo simplificado

class ExameRaioX(Exame):
    def __init__(self):
        self.tipo = "raio-x"

    def verificar_condicoes(self):
        # Implementação específica para raio-x
        return True  # Exemplo simplificado

class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verificar_condicoes():
            print(f"Exame de {exame.tipo} aprovado!")
        else:
            print(f"Exame de {exame.tipo} não aprovado!")

# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)


