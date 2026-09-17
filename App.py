import pandas as pd

df = pd.read_excel("Report-Consolidado-16-09-2026.xlsx")
colunas = ["Valor Total c/ Desconto", "Custo Total", "Lucro"]
df_produto = df.groupby("País")[colunas].sum().round(2)
df_produto["Margem lucro"] = round((df_produto["Lucro"] / df_produto[("Valor Total c/ Desconto")]) * 100, 2)
print(df_produto)