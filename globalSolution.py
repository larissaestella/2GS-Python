import datetime
import json

class MonitoramentoOceano:
    def __init__(self, id_barco):
        self.id_barco = id_barco
        self.registro_dados = []

    def coletar_dados(self):
        # Coletar dados via input do usuário
        try:
            plastico_detectado = float(input(f"Digite a quantidade de plástico detectado (kg/km²) para o barco {self.id_barco}: "))
            temperatura_agua = float(input(f"Digite a temperatura da água (Celsius) para o barco {self.id_barco}: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira valores numéricos.")
            return None

        dados = {
            'timestamp': datetime.datetime.now().isoformat(),
            'id_barco': self.id_barco,
            'plastico_detectado': plastico_detectado,
            'temperatura_agua': temperatura_agua
        }
        self.registro_dados.append(dados)
        return dados

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(self.registro_dados, arquivo, indent=4)
        print(f"Dados salvos em {nome_arquivo}")

class ProgramaReciclagemEscola:
    def __init__(self, nome_escola):
        self.nome_escola = nome_escola
        self.materiais_coletados = {}
        self.fundos = 0
        self.registro_vendas = []

    def coletar_material(self):
        # Coletar dados via input do usuário
        material = input(f"Digite o tipo de material coletado na escola {self.nome_escola} (ex: garrafas PET, sacolas plásticas): ")
        try:
            peso = float(input(f"Digite o peso (kg) do material {material} coletado: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico para o peso.")
            return

        if material in self.materiais_coletados:
            self.materiais_coletados[material] += peso
        else:
            self.materiais_coletados[material] = peso
        print(f"Coletados {peso} kg de {material}")

    def vender_materiais(self):
        try:
            preco_por_kg = float(input(f"Digite o preço por kg dos materiais recicláveis para a escola {self.nome_escola}: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico para o preço por kg.")
            return

        peso_total = sum(self.materiais_coletados.values())
        fundos = peso_total * preco_por_kg
        self.fundos += fundos

        venda = {
            'timestamp': datetime.datetime.now().isoformat(),
            'materiais_coletados': self.materiais_coletados.copy(),
            'preco_por_kg': preco_por_kg,
            'fundos': fundos
        }
        self.registro_vendas.append(venda)

        print(f"Vendidos {peso_total} kg de materiais por R${fundos:.2f}")
        self.materiais_coletados = {}  # Resetar após a venda

    def obter_fundos(self):
        return self.fundos

    def salvar_dados(self, nome_arquivo):
        dados = {
            'nome_escola': self.nome_escola,
            'fundos': self.fundos,
            'registro_vendas': self.registro_vendas
        }
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f"Dados salvos em {nome_arquivo}")

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

    def coletar_material_escola(self, nome_escola):
        if nome_escola in self.programas_escolas:
            self.programas_escolas[nome_escola].coletar_material()
        else:
            print(f"Escola {nome_escola} não encontrada")

    def vender_materiais_escola(self, nome_escola):
        if nome_escola in self.programas_escolas:
            self.programas_escolas[nome_escola].vender_materiais()
        else:
            print(f"Escola {nome_escola} não encontrada")

    def salvar_dados_oceano(self, id_barco, nome_arquivo):
        if id_barco in self.monitores_barcos:
            self.monitores_barcos[id_barco].salvar_dados(nome_arquivo)
        else:
            print(f"ID do barco {id_barco} não encontrado")

    def salvar_dados_escola(self, nome_escola, nome_arquivo):
        if nome_escola in self.programas_escolas:
            self.programas_escolas[nome_escola].salvar_dados(nome_arquivo)
        else:
            print(f"Escola {nome_escola} não encontrada")

    def obter_fundos_escola(self, nome_escola):
        if nome_escola in self.programas_escolas:
            return self.programas_escolas[nome_escola].obter_fundos()
        else:
            print(f"Escola {nome_escola} não encontrada")
            return None

# Exemplo de uso
projeto = ProjetoAmbiental()
projeto.adicionar_barco("Barco_123")
projeto.adicionar_escola("Escola Verde")

# Coleta de dados do oceano via input do usuário
for _ in range(2):  # Coleta 2 pontos de dados como exemplo
    dados = projeto.coletar_dados_oceano("Barco_123")
    print(dados)

projeto.salvar_dados_oceano("Barco_123", "dados_oceano.json")

# Coleta de materiais recicláveis na escola via input do usuário
for _ in range(2):  # Coleta materiais 2 vezes como exemplo
    projeto.coletar_material_escola("Escola Verde")

projeto.vender_materiais_escola("Escola Verde")
print(f"Total de fundos arrecadados pela Escola Verde: R${projeto.obter_fundos_escola('Escola Verde'):.2f}")

# Salvar dados da escola em um arquivo JSON
projeto.salvar_dados_escola("Escola Verde", "dados_escola.json")
