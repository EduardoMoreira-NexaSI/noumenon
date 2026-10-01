"""
NOUMENON - Experimento 001

Primeira estrutura criada para visualização do projeto.
Mundo multidimensional + observador limitado.
"""

from dataclasses import dataclass


@dataclass
class Ponto4D:
    x: float
    y: float
    z: float
    w: float


class Mundo:
    def __init__(self, nome):
        self.nome = nome
        self.dimensoes = ["x", "y", "z", "w"]
        self.tempo = 0.0
        self.pontos = []

    def adicionar_ponto(self, ponto):
        self.pontos.append(ponto)


@dataclass
class Observacao:
    observador_id: int
    tempo: float
    valores: dict[str, float]


class Observador:
    def __init__(self, observador_id, dimensoes_acessiveis):
        self.id = observador_id
        self.dimensoes_acessiveis = dimensoes_acessiveis
        self.memoria = []

    def observar(self, ponto, tempo):
        valores = {}

        for dimensao in self.dimensoes_acessiveis:
            valores[dimensao] = getattr(ponto, dimensao)

        observacao = Observacao(
            observador_id=self.id,
            tempo=tempo,
            valores=valores
        )

        self.memoria.append(observacao)

        return observacao


mundo_a = Mundo("Mundo A")

dimensoes_acessiveis = ["x", "y", "z"]
observador_a = Observador(1, dimensoes_acessiveis)

ponto_real = Ponto4D(3, 6, 9, 18)
mundo_a.adicionar_ponto(ponto_real)

observacao = observador_a.observar(
    ponto_real,
    mundo_a.tempo
)

print(f"Mundo: {mundo_a.nome}")
print(f"Dimensões: {mundo_a.dimensoes}")
print(f"Ponto real: {ponto_real}")
print(f"Resultado OBSERVAÇÃO: {observacao}")
print(f"MEMÓRIA DO OBSERVADOR: {observador_a.memoria}")