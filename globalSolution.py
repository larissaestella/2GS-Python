import random
import datetime
import json

class MonitoramentoOceano:
    def __init__(self, id_barco):
        self.id_barco = id_barco
        self.registro_dados = []

    def coletar_dados(self):
        # Simular a coleta de dados
        dados = {
            'timestamp': datetime.datetime.now().isoformat(),
            'id_barco': self.id_barco,
            'plastico_detectado': random.uniform(0, 5),  # kg/km²
            'temperatura_agua': random.uniform(15, 30)  # Celsius
        }
        self.registro_dados.append(dados)
        return dados

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(self.registro_dados, arquivo, indent=4)
        print(f"Dados salvos em {nome_arquivo}")

monitoramento_barco = MonitoramentoOceano(id_barco="Barco_123")
for _ in range(10):  # Simular 10 pontos de dados
    dados = monitoramento_barco.coletar_dados()
    print(dados)

monitoramento_barco.salvar_dados("dados_oceano.json")


class ProgramaReciclagemEscola:
    def __init__(self, nome_escola):
        self.nome_escola = nome_escola
        self.materiais_coletados = {}
        self.fundos = 0

    def coletar_material(self, material, peso):
        if material in self.materiais_coletados:
            self.materiais_coletados[material] += peso
        else:
            self.materiais_coletados[material] = peso
        print(f"Coletados {peso} kg de {material}")

    def vender_materiais(self, preco_por_kg):
        peso_total = sum(self.materiais_coletados.values())
        ganhos = peso_total * preco_por_kg
        self.fundos += ganhos
        print(f"Vendidos {peso_total} kg de materiais por R${ganhos:.2f}")
        self.materiais_coletados = {}  # Resetar após a venda

    def obter_fundos(self):
        return self.fundos

programa_escola = ProgramaReciclagemEscola(nome_escola="Escola Verde")
programa_escola.coletar_material("plástico", 10)
programa_escola.coletar_material("alumínio", 5)
programa_escola.coletar_material("plástico", 2)

programa_escola.vender_materiais(preco_por_kg=0.5)
print(f"Total de fundos arrecadados: R${programa_escola.obter_fundos():.2f}")



class ProjetoAmbiental:
    def __init__(self):
        self.monitores_barcos = {}
        self.programas_escolas = {}

    def adicionar_barco(self, id_barco):
        self.monitores_barcos[id_barco] = MonitoramentoOceano(id_barco)

    def adicionar_escola(self, nome_escola):
        self.programas_escolas[nome_escola] = ProgramaReciclagemEscola(nome_escola)

    def coletar_dados_oceano(self, id_barco):
        if id_barco in self.monitores_barcos:
            return self.monitores_barcos[id_barco].coletar_dados()
        else:
            print(f"ID do barco {id_barco} não encontrado")
            return None

    def coletar_material_escola(self, nome_escola, material, peso):
        if nome_escola in self.programas_escolas:
            self.programas_escolas[nome_escola].coletar_material(material, peso)
        else:
            print(f"Escola {nome_escola} não encontrada")

    def vender_materiais_escola(self, nome_escola, preco_por_kg):
        if nome_escola in self.programas_escolas:
            self.programas_escolas[nome_escola].vender_materiais(preco_por_kg)
        else:
            print(f"Escola {nome_escola} não encontrada")

    def salvar_dados_oceano(self, id_barco, nome_arquivo):
        if id_barco in self.monitores_barcos:
            self.monitores_barcos[id_barco].salvar_dados(nome_arquivo)
        else:
            print(f"ID do barco {id_barco} não encontrado")

    def obter_fundos_escola(self, nome_escola):
        if nome_escola in self.programas_escolas:
            return self.programas_escolas[nome_escola].obter_fundos()
        else:
            print(f"Escola {nome_escola} não encontrada")
            return None

projeto = ProjetoAmbiental()
projeto.adicionar_barco("Barco_123")
projeto.adicionar_escola("Escola Verde")

for _ in range(3):  # Simular 10 pontos de dados
    dados = projeto.coletar_dados_oceano("Barco_123")
    print(dados)

projeto.salvar_dados_oceano("Barco_123", "dados_oceano.json")

projeto.coletar_material_escola("Escola Verde", "plástico", 10)
projeto.coletar_material_escola("Escola Verde", "alumínio", 5)
projeto.coletar_material_escola("Escola Verde", "plástico", 2)

projeto.vender_materiais_escola("Escola Verde", preco_por_kg=0.5)
print(f"Total de fundos arrecadados pela Escola Verde: R${projeto.obter_fundos_escola("Escola Verde"):.2f}")
