import pandas as pd

arquivo = "dados/CONTROLE DE ESTOQUE (ORIGINA) (Reparado)(1).xlsx"

df = pd.read_excel(arquivo)

print(df.columns.tolist())
