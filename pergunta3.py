import pandas as pd

#Extração das Datas da medição, Vazão Natural Consolidada, Vazão Incremental Consolidada de medições de um posto
df = pd.read_excel("ACOMPH_12.05.2020.xls", sheet_name = 0, usecols = [0,7,8], skiprows=4, nrows=30)

#Extraindo Nome de um posto
nome_posto = pd.read_excel("ACOMPH_12.05.2020.xls", sheet_name = 0, usecols = [1], skiprows=1, nrows=1)
nome_posto = nome_posto.columns.values.tolist()

#Extraindo Código de um posto
cod_posto = pd.read_excel("ACOMPH_12.05.2020.xls", sheet_name = 0, usecols = [8], skiprows=0, nrows=1)
cod_posto = cod_posto.columns.values.tolist()

#Lista auxiliar para criação das colunas de Nome e Código de um posto no DataFrame
for i in range(29):
    nome_posto.append(nome_posto[0])
    cod_posto.append(cod_posto[0])

#Renomeando colunas do DataFrame
df['Nome do Posto'] = nome_posto
df['Código do Posto'] = cod_posto
df.rename(columns={'Unnamed: 0': 'Data da Medição','Consol.3': 'Vazão Incremental Consolidada', 'Consol.4': 'Vazão Natural Consolidada'}, inplace = True)

print(df)
