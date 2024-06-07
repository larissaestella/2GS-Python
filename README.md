# Global Solution - 2 SEMESTRE

            Jeferson Gabriel de Mendonça | 553149 
            Larissa Estella Gonçalves dos Santos | 552695
            Victor Henrique Vilares Rodrigues | 554175

## Descrição do Projeto

Este é um programa Python de um projeto que tem como objetivo reduzir a quantidade de resíduos plásticos nos oceanos e promover a conscientização e educação ambiental nas escolas. Ele é dividido em duas partes principais:

1. **Monitoramento dos Resíduos Plásticos no Oceano**: Utiliza sensores instalados em barcos para detectar plásticos na superfície do oceano e medir a temperatura da água.
2. **Conscientização e Educação Ambiental nas Escolas**: Envolve alunos na coleta de materiais recicláveis, que são vendidos a centros de reciclagem, revertendo os ganhos para projetos educativos e sustentáveis.

## Funcionalidades

### Monitoramento dos Resíduos Plásticos nos Oceanos

- **Coleta de Dados**: Sensores em barcos coletam dados sobre a quantidade de plástico e a temperatura da água.
- **Armazenamento de Dados**: Os dados coletados são armazenados com um timestamp para análise futura.
- **Geração de Relatórios**: Dados podem ser salvos em um arquivo JSON para posterior análise e visualização.

### Conscientização e Educação Ambiental nas Escolas

- **Coleta de Materiais Recicláveis**: Alunos coletam e registram materiais recicláveis como plástico e alumínio.
- **Venda de Materiais**: Materiais coletados são vendidos a centros de reciclagem, gerando fundos para a escola.
- **Gestão de Fundos**: Os recursos obtidos são usados para financiar atividades educativas e projetos de sustentabilidade.

## Estrutura do Código

### `globalSolution.py`

Contém a implementação das classes e funções principais:

- **`MonitoramentoOceano`**: Classe para gerenciar a coleta e armazenamento de dados do oceano.
- **`ProgramaReciclagemEscola`**: Classe para gerenciar a coleta de materiais recicláveis e a gestão de fundos nas escolas.
- **`ProjetoAmbiental`**: Classe que integra as funcionalidades de monitoramento dos oceanos e reciclagem nas escolas.

### Classes e Funções

1. **Classe `MonitoramentoOceano`**
   - **`__init__(self, id_barco)`**: Inicializa a instância com o ID do barco e uma lista vazia para registrar dados.
   - **`coletar_dados(self)`**: Coleta a quantidade de plástico detectado e a temperatura da água via input do usuário.
   - **`salvar_dados(self, nome_arquivo)`**: Salva os dados coletados em um arquivo JSON.

2. **Classe `ProgramaReciclagemEscola`**
   - **`__init__(self, nome_escola)`**: Inicializa a instância com o nome da escola, um dicionário para materiais coletados, um valor inicial de fundos e uma lista para registrar vendas.
   - **`coletar_material(self)`**: Coleta o tipo e o peso do material reciclável via input do usuário.
   - **`vender_materiais(self)`**: Coleta o preço por kg dos materiais recicláveis via input do usuário, calcula o total de fundos arrecadados e registra a venda.
   - **`obter_fundos(self)`**: Retorna o total de fundos arrecadados pela escola.
   - **`salvar_dados(self, nome_arquivo)`**: Salva os dados coletados e os fundos arrecadados em um arquivo JSON.

3. **Classe `ProjetoAmbiental`**
   - **`__init__(self)`**: Inicializa o projeto com dicionários vazios para monitores de barcos e programas de escolas.
   - **`adicionar_barco(self, id_barco)`**: Adiciona um novo barco ao monitoramento.
   - **`adicionar_escola(self, nome_escola)`**: Adiciona uma nova escola ao programa de reciclagem.
   - **`coletar_dados_oceano(self, id_barco)`**: Coleta dados de resíduos plásticos e temperatura da água para um barco específico.
   - **`coletar_material_escola(self, nome_escola)`**: Coleta materiais recicláveis para uma escola específica.
   - **`vender_materiais_escola(self, nome_escola)`**: Vende materiais recicláveis e calcula os fundos arrecadados para uma escola específica.
   - **`salvar_dados_oceano(self, id_barco, nome_arquivo)`**: Salva os dados de um barco específico em um arquivo JSON.
   - **`salvar_dados_escola(self, nome_escola, nome_arquivo)`**: Salva os dados de uma escola específica em um arquivo JSON.
   - **`obter_fundos_escola(self, nome_escola)`**: Retorna o total de fundos arrecadados por uma escola específica.

## Instruções de Uso

### Pré-requisitos

- Python 3
- Biblioteca `json`

### Como Executar

Abra o terminal/Prompt de Comando

1. **Navegue até o diretório** onde o arquivo `globalSolution.py` está localizado.

2. **Execute o script**: usando o seguinte comando no terminal 

    ```sh
    python globalSolution.py
    ```

3. **Interaja com o programa**:
   - Para barcos, insira a quantidade de plástico detectado e a temperatura da água.
   - Para escolas, insira o tipo de material coletado, o peso do material e o preço por kg dos materiais recicláveis.

4. **Os dados serão salvos** em arquivos JSON chamados `dados_oceano.json` e `dados_escola.json`.

5. **Resultados Esperados**:
    - Dados de monitoramento do oceano serão exibidos no terminal e salvos em um arquivo JSON.
    - Informações sobre materiais recicláveis coletados e fundos gerados serão exibidas no terminal e salvos em um arquivo JSON.

## Detalhes dos Arquivos JSON

### `dados_oceano.json`
Armazena os dados coletados dos barcos, incluindo:
- `timestamp`: Data e hora da coleta.
- `id_barco`: Identificação do barco.
- `plastico_detectado`: Quantidade de plástico detectado (kg/km²).
- `temperatura_agua`: Temperatura da água (Celsius).

### `dados_escola.json`
Armazena os dados coletados das escolas, incluindo:
- `nome_escola`: Nome da escola.
- `fundos`: Total de fundos arrecadados.
- `registro_vendas`: Lista de registros de vendas, cada um contendo:
  - `timestamp`: Data e hora da venda.
  - `materiais_coletados`: Dicionário com tipos de materiais e seus pesos (kg).
  - `preco_por_kg`: Preço por kg dos materiais recicláveis.
  - `ganhos`: Total arrecadado com a venda.




