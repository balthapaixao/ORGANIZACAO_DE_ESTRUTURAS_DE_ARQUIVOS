##Balthazar Paixão
#
##
###
####
###
##
#
import pandas as pd

df = pd.read_csv('bolsa.csv', encoding='latin1', sep = '\t')
df2 = pd.read_csv('bolsa10.csv', encoding= 'latin1', sep = '\t')

a = pd.DataFrame(df[df["NIS Favorecido"].isin(df2["NIS Favorecido"])]) # Operação ce conjunto

#tive que apelar pra gambiarra
dic0 = {}
dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}
dic5 = {}
dic6 = {}
dic7 = {}
dic8 = {}

for coluna in a:
    for i in a[coluna]:
        dic0[coluna] = a[coluna][0]
        dic1[coluna] = a[coluna][1]
        dic2[coluna] = a[coluna][2]
        dic3[coluna] = a[coluna][3]
        dic4[coluna] = a[coluna][4]
        dic5[coluna] = a[coluna][5]
        dic6[coluna] = a[coluna][6]
        dic7[coluna] = a[coluna][7]
        dic8[coluna] = a[coluna][8]

text = str(str(dic0) + '\n' + str(dic1) + '\n' + str(dic2) + '\n' + str(dic3) + '\n' + str(dic4) + '\n' + str(dic5) + '\n' + str(dic6) + '\n' + str(dic7) + '\n' + str(dic8))

with open("saida.txt", 'w') as f:
    f.write(text)
f.close()