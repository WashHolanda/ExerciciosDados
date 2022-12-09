import pandas as pd

#Importação das bases para o Python
tbl_vazao = pd.read_csv("tbl_vazao.csv")
tbl_postos = pd.read_csv("tbl_postos.csv")

#Junção das duas bases usando a coluna 'num_posto' como chave primária
merge = pd.merge(tbl_vazao, tbl_postos, how = 'outer', on='num_posto')

#Filtragem dos postos de medição que possuem valor 1 na variável 'bin_ena'
base_filtrada = merge.loc[merge['bin_ena'] == 1]

#Inserção da coluna do Calculo do ENA de cada posto de medição e da coluna mês de cada data de medição
base_filtrada['ENA'] = base_filtrada['val_vaz_natr'] * base_filtrada['val_produt']
base_filtrada['mes'] = pd.DatetimeIndex(base_filtrada['dat_medicao']).month

#Agregação e visualização dos dados de ENA por subsistema
print("\nMédia diária do ENA de cada subsistema:\n")
base_agregadaMD = base_filtrada.groupby(['nom_ssis', 'dat_medicao', 'mes']).agg({'ENA':'mean'})
print(base_agregadaMD)

print("\nMédia mensal diária do ENA de cada subsistema:\n")
base_agregadaMMD = base_agregadaMD.groupby(['nom_ssis', 'mes']).agg({'ENA':'mean'})
print(base_agregadaMMD)
