# Análise de Chamados de Manutenção

Projeto de análise de dados desenvolvido com **Python, Pandas e Power BI**, utilizando uma base de dados fictícia criada para fins educacionais.

O projeto simula o acompanhamento de chamados de manutenção e busca transformar dados brutos em informações que possam auxiliar na análise de **volume de chamados, custos, status, prioridades, unidades e tempo de resolução**.

> **Observação:** todos os dados utilizados neste projeto são fictícios e foram gerados artificialmente para fins de estudo e demonstração de habilidades em análise de dados.

---

## Objetivo

O objetivo do projeto é praticar um fluxo completo de análise de dados, desde a **geração e tratamento da base** até a criação de um **dashboard interativo no Power BI**.

O projeto foi desenvolvido para demonstrar conhecimentos em:

* Manipulação e tratamento de dados com Python e Pandas;
* Análise exploratória de dados;
* Criação de indicadores;
* Visualização de dados;
* Construção de dashboards interativos;
* Organização de um projeto de análise de dados;
* Documentação de resultados para apresentação em portfólio.

---

## Tecnologias utilizadas

### Python

Utilizado para geração, tratamento e análise da base de dados.

### Pandas

Utilizado para:

* leitura dos arquivos CSV;
* tratamento dos dados;
* agrupamentos;
* cálculos estatísticos;
* criação de indicadores;
* preparação da base utilizada no Power BI.

### Matplotlib

Utilizado para criação de visualizações durante a análise exploratória.

### Jupyter Notebook

Utilizado para documentar e executar as etapas da análise exploratória.

### Power BI

Utilizado para criação do dashboard interativo, indicadores, gráficos e filtros.

### Git e GitHub

Utilizados para versionamento e publicação do projeto.

---

## Estrutura do projeto

```text
analiseMhamadosManutencao/
│
├── dados/
│   ├── chamadosManutencao.csv
│   ├── chamadosManutencaoTratados.csv
│   ├── chamadosPorStatus.csv
│   ├── chamadosPorTipo.csv
│   ├── chamadosPorUnidade.csv
│   └── baseFinalPowerbi.csv
│
├── notebooks/
│   └── 01analiseInicial.ipynb
│
├── dashboard/
│   └── analiseChamadosManutencao.pbix
│
├── gerar_dados.py
├── requirements.txt
└── .gitignore
```

---

## Fluxo do projeto

O projeto foi desenvolvido seguindo as seguintes etapas:

```text
Geração dos dados
       ↓
Tratamento da base
       ↓
Análise exploratória
       ↓
Criação dos indicadores
       ↓
Preparação da base para o Power BI
       ↓
Criação do dashboard
       ↓
Análise dos resultados
```

---

## Base de dados

A base contém **500 chamados de manutenção fictícios**.

Entre as informações disponíveis estão:

| Campo                     | Descrição                      |
| ------------------------- | ------------------------------ |
| `idChamado`               | Identificador do chamado       |
| `dataAbertura`            | Data de abertura               |
| `unidade`                 | Unidade relacionada ao chamado |
| `tipoManutencao`          | Tipo de manutenção             |
| `prioridade`              | Prioridade do chamado          |
| `status`                  | Situação do chamado            |
| `categoriaProblema`       | Categoria do problema          |
| `tecnico`                 | Técnico responsável            |
| `tempoAtendimentoHoras`   | Tempo de atendimento           |
| `tempoResolucaoHoras`     | Tempo de resolução             |
| `custo`                   | Custo associado ao chamado     |
| `mes`                     | Mês de abertura                |
| `numeroMes`               | Número correspondente ao mês   |

As unidades utilizadas na simulação são:

* Guaíba
* Porto Alegre
* Canoas
* Gravataí
* Alvorada

Os tipos de manutenção utilizados são:

* Preventiva
* Corretiva
* Preditiva

---

##  Tratamento dos dados

Após a geração da base, foram realizadas verificações para garantir a consistência dos dados utilizados na análise.

Foram verificadas:

* existência de valores ausentes;
* existência de registros duplicados;
* valores inválidos de tempo;
* custos negativos;
* conversão da coluna de data para o formato adequado;
* criação de informações auxiliares de mês;
* preparação da base final utilizada no Power BI.

A base tratada foi posteriormente exportada em CSV para utilização no dashboard.

---

##  Análise realizada

A análise exploratória buscou responder algumas perguntas relacionadas aos chamados de manutenção.

### Volume de chamados

Foi analisada a quantidade de chamados:

* por status;
* por tipo de manutenção;
* por unidade;
* por mês;
* por prioridade.

### Custos

Foram analisados:

* custo total;
* custo por unidade;
* custo total por tipo de manutenção;
* custo médio por chamado de cada tipo de manutenção.

### Tempo de resolução

Foi analisado o tempo médio necessário para resolução dos chamados, incluindo uma comparação entre as diferentes prioridades.

Também foi explorada visualmente a relação entre **tempo de resolução e custo**.

---

##  Principais indicadores

A base analisada apresentou os seguintes indicadores:

| Indicador                |         Resultado |
| ------------------------ | ----------------: |
| Total de chamados        |           **500** |
| Chamados concluídos      |        **32,80%** |
| Custo total              | **R$ 768.151,01** |
| Tempo médio de resolução |   **30,24 horas** |

### Tempo médio de resolução por prioridade

| Prioridade | Tempo médio |
| ---------- | ----------: |
| Alta       |     31,27 h |
| Crítica    |     31,11 h |
| Baixa      |     30,79 h |
| Média      |     27,73 h |

---

##  Observações encontradas na análise

A análise da base fictícia apresentou alguns padrões:

* **Corretiva** foi o tipo de manutenção com maior quantidade de chamados e também apresentou o maior custo total.
* **Preventiva** apresentou o maior custo médio por chamado.
* **Julho** foi o mês com maior quantidade de chamados.
* O tempo médio de resolução apresentou valores próximos entre algumas categorias de prioridade.
* A relação entre custo e tempo de resolução apresentou uma distribuição bastante espalhada, sem uma relação visual evidente na análise realizada.

> Como os dados foram gerados artificialmente, esses padrões representam apenas o comportamento da base simulada e não devem ser interpretados como conclusões sobre operações reais.

---

##  Dashboard

O dashboard desenvolvido no Power BI apresenta:

### Indicadores

* Total de chamados;
* Percentual de chamados concluídos;
* Custo total;
* Tempo médio de resolução.

### Gráficos

* Chamados por mês;
* Custo total por tipo de manutenção;
* Chamados por unidade;
* Tempo médio de resolução por prioridade.

### Filtros interativos

O usuário pode filtrar os dados por:

* Unidade;
* Tipo de manutenção;
* Prioridade;
* Status.

Os filtros atualizam os indicadores e visualizações do dashboard de acordo com a seleção realizada.

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/DanieliPradoNunes/analise-chamados-manutencao.git
```

Depois, entre na pasta:

```bash
cd analiseChamadosManutencao
```

---

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Gerar a base de dados

Execute:

```bash
python gerarDados.py
```

O script irá gerar a base de chamados dentro da pasta `dados/`.

---

### 5. Executar a análise

Abra o Jupyter Notebook:

```bash
jupyter notebook
```

Depois, abra:

```text
notebooks/01analiseInicial.ipynb
```

Execute as células do notebook para acompanhar as etapas de tratamento, análise e visualização dos dados.

---

### 6. Visualizar o dashboard

Abra o arquivo:

```text
dashboard/analise_chamados_manutencao.pbix
```

com o **Power BI Desktop**.

---

##  Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos relacionados a:

* geração e organização de dados;
* limpeza e validação de bases;
* manipulação de DataFrames;
* agrupamento e agregação de informações;
* análise exploratória;
* criação de indicadores;
* visualização de dados;
* construção de dashboards;
* utilização de filtros interativos;
* organização de projetos para portfólio;
* documentação técnica.

---


