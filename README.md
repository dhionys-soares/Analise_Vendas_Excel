# 📊 Análise de Vendas com Python e Excel

Projeto desenvolvido em **Python** para análise de dados de vendas a partir de uma base Excel.

A aplicação utiliza **Pandas** para leitura, agrupamento e processamento dos dados, permitindo analisar indicadores financeiros por país, como **valor total das vendas, custo, lucro e margem de lucro**.

## 🎯 Objetivo

O objetivo do projeto é praticar e demonstrar conceitos de **análise e manipulação de dados com Python**, utilizando uma planilha Excel como fonte de dados.

A análise busca responder perguntas como:

* 💰 Qual o valor total vendido por país?
* 📦 Qual o custo total das vendas?
* 📈 Qual o lucro obtido?
* 📊 Qual a margem de lucro de cada país?

## 🛠️ Tecnologias utilizadas

* 🐍 **Python**
* 🐼 **Pandas**
* 📗 **Excel**
* 🔧 **PyCharm / VS Code**
* 🌱 **Git e GitHub**

## ⚙️ Funcionamento

O script realiza as seguintes etapas:

1. 📂 Leitura do arquivo Excel utilizando `pandas.read_excel()`;
2. 🔎 Seleção das colunas relevantes para a análise;
3. 🌎 Agrupamento dos dados por **País**;
4. ➕ Soma dos valores de vendas, custos e lucros;
5. 📐 Cálculo da margem de lucro;
6. 🖥️ Exibição dos resultados no terminal.

### 📌 Indicadores calculados

| Indicador                   | Descrição                                             |
| --------------------------- | ----------------------------------------------------- |
| **Valor Total c/ Desconto** | Total das vendas após os descontos                    |
| **Custo Total**             | Custo total associado às vendas                       |
| **Lucro**                   | Resultado financeiro das vendas                       |
| **Margem de lucro**         | Percentual de lucro em relação ao valor total vendido |

A margem de lucro é calculada utilizando:

```python
Margem de lucro = (Lucro / Valor Total c/ Desconto) × 100
```

## 📁 Estrutura do projeto

```text
Analise_Vendas_Excel/
│
├── 📄 App.py
├── 📊 Report-Consolidado-16-09-2026.xlsx
├── 📄 README.md
└── 🚫 .gitignore
```

### `App.py`

Arquivo principal responsável pela leitura e análise dos dados.

O código utiliza `groupby()` para consolidar os indicadores por país:

```python
df_produto = df.groupby("País")[colunas].sum().round(2)
```

Em seguida, calcula a margem de lucro:

```python
df_produto["Margem lucro"] = round(
    (df_produto["Lucro"] / df_produto["Valor Total c/ Desconto"]) * 100,
    2
)
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/dhionys-soares/Analise_Vendas_Excel.git
```

### 2. Acesse a pasta

```bash
cd Analise_Vendas_Excel
```

### 3. Instale as dependências

Caso ainda não tenha o Pandas instalado:

```bash
pip install pandas openpyxl
```

### 4. Execute o projeto

```bash
python App.py
```

O resultado da análise será exibido diretamente no terminal.

## 📊 Exemplo da análise

A aplicação consolida os dados por país, produzindo uma estrutura semelhante a:

```text
                    Valor Total c/ Desconto   Custo Total     Lucro   Margem lucro
País
Brasil                         ...              ...           ...          ...%
...
```

## 📚 Conceitos praticados

Este projeto foi desenvolvido como prática de:

* Manipulação de dados com **Pandas**
* Leitura de arquivos **Excel**
* Agrupamento de dados com `groupby()`
* Agregação de valores com `sum()`
* Criação de métricas calculadas
* Cálculos financeiros com Python
* Formatação e análise de dados
* Organização de projetos Python
* Versionamento com Git e GitHub

## 🚧 Próximas melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* 📊 Criação de gráficos para visualização dos indicadores;
* 📈 Análise de evolução das vendas ao longo do tempo;
* 🏆 Ranking de países por vendas e lucro;
* 🔍 Filtros para diferentes categorias de produtos;
* 💾 Exportação dos resultados para um novo arquivo Excel;
* 📑 Geração de um relatório consolidado;
* 🌐 Transformação da análise em um dashboard interativo.

## 👨‍💻 Autor

**Dhionys Soares**

Estudante de Engenharia de Software e desenvolvedor com foco em **.NET, Python, APIs, banco de dados e análise de dados**.

---

⭐ Projeto desenvolvido para fins de estudo e construção de portfólio.
