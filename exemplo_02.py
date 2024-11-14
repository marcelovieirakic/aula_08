import pandas as pd

df_clientes = pd.read_csv("Data/clientes.csv") #dataframe
df_vendas_1 = pd.read_csv("Data/vendas.csv") #dataframe
df_vendas_2 = pd.read_csv("Data/vendas_2.csv") #dataframe
df_vendas_3 = pd.read_csv("Data/vendas_3.csv") #dataframe

# print(df_clientes.head(5)) #limitar quantidade linhas visualizadas
# print(df_vendas_1.head(5))
# print(df_vendas_2.head(5))
# print(df_vendas_3.head(5))

df_uniao = pd.concat([df_vendas_1,df_vendas_2,df_vendas_3], ignore_index=True) #union all --> ignore index parametro do metodo concatenar
df_upper = df_uniao.rename(str.upper, axis="columns")
df_colunas_renomeada = df_upper.rename(columns={'VENDA_ID': 'CHAVE_VENDA', "CLIENTE_ID": "CHAVE_CLIENTE"})
df_colunas_renomeada.to_csv("Data/vendas_unida.csv", index=False)
print(df_colunas_renomeada.shape) #linhas x colunas qtd

df_completo = pd.merge(df_clientes, df_colunas_renomeada, left_on="cliente_id", right_on="CHAVE_CLIENTE")
print(df_completo)

df_completo.to_excel("Data/uniao.xlsx")