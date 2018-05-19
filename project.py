from pandas import read_csv

camara2018jan = read_csv('./data/tcm-ba/camara/2018-01.csv')

def converteSalarioEmFloat(dados, coluna):
    dados[coluna] = dados[coluna].str.replace('.','').str.replace(',','.').astype('float')

# Converte as colunas de salários em tipo float para realização dos cálculos
converteSalarioEmFloat(camara2018jan, 'Salário Base')
converteSalarioEmFloat(camara2018jan, 'Salário Vantagens')
converteSalarioEmFloat(camara2018jan, 'Salário Gratificação')

#Cria nova coluna com o total de cada salário
camara2018jan['Salário Total'] = camara2018jan['Salário Base'] + camara2018jan['Salário Vantagens'] + camara2018jan['Salário Gratificação']

# Imprime a soma de todos os salários
print("Soma dos salários: ", camara2018jan['Salário Total'].sum(),"\n")

# Imprime a linha com o maior Salário Total
print(camara2018jan.loc[camara2018jan['Salário Total'].idxmax()],"\n")

# Encontra os nomes dos cargos existentes
cargos = camara2018jan['Cargo'].dropna().unique()

# Para cada cargo, imprime a linha com o maior salário total
for cargo in cargos:
    apenas_cargo_escolhido = camara2018jan.loc[camara2018jan['Cargo'] == cargo]
    maior_salario_do_cargo = apenas_cargo_escolhido.loc[apenas_cargo_escolhido['Salário Total'].idxmax()]
    print("Cargo: ",cargo)
    print(maior_salario_do_cargo[['Nome', 'Salário Total']],"\n")
