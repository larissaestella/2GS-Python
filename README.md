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

### Classes

#### `MonitoramentoOceano`

- **`__init__(self, id_barco)`**: Inicializa a classe com um ID de barco.
- **`coletar_dados(self)`**: Coleta a quantidade de plástico detectado e a temperatura da água via input do usuário.
- **`salvar_dados(self, nome_arquivo)`**: Salva os dados coletados em um arquivo JSON.

#### `ProgramaReciclagemEscola`

- **`__init__(self, nome_escola)`**: Inicializa a classe com o nome da escola.
- **`coletar_material(self)`**: Coleta o tipo e peso de materiais recicláveis via input do usuário.
- **`vender_materiais(self)`**: Calcula e registra os fundos obtidos com a venda de materiais recicláveis, reiniciando o registro de materiais após a venda.
- **`obter_fundos(self)`**: Retorna o total de fundos arrecadados.

#### `ProjetoAmbiental`

- **`__init__(self)`**: Inicializa a classe.
- **`adicionar_barco(self, id_barco)`**: Adiciona um barco ao projeto.
- **`adicionar_escola(self, nome_escola)`**: Adiciona uma escola ao projeto.
- **`coletar_dados_oceano(self, id_barco)`**: Coleta dados de um barco específico via input do usuário.
- **`coletar_material_escola(self, nome_escola)`**: Coleta materiais recicláveis de uma escola específica via input do usuário.
- **`vender_materiais_escola(self, nome_escola)`**: Vende os materiais coletados e atualiza os fundos da escola.
- **`salvar_dados_oceano(self, id_barco, nome_arquivo)`**: Salva os dados coletados por um barco em um arquivo JSON.
- **`obter_fundos_escola(self, nome_escola)`**: Obtém os fundos arrecadados por uma escola.

## Instruções de Uso

### Pré-requisitos

- Python 3
- Editor de texto ou IDE de sua preferência


### Como Executar

Abra o terminal/Prompt de Comando

1. **Execute o script**:

    ```sh
    python globalSolution.py
    ```

- O terminal irá pedir para você inserir a quantidade de plástico detectado e a temperatura da água para o barco.
- Os dados coletados serão salvos em um arquivo JSON chamado `dados_oceano.json`.
- Em seguida, você precisará inserir os tipos de materiais recicláveis e seus pesos coletados na escola.
- Após a coleta, o programa pedirá o preço por kg dos materiais recicláveis para calcular os ganhos.
- Os dados coletados serão salvos em um arquivo JSON chamado `dados_escola.json`

2. **Resultados Esperados**:
    - Dados de monitoramento do oceano serão exibidos no terminal e salvos em um arquivo JSON.
    - Informações sobre materiais recicláveis coletados e fundos gerados serão exibidas no terminal e salvos em um arquivo JSON.



