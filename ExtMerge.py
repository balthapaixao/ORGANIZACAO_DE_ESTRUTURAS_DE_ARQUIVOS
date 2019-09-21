##Balthazar Paixão
#
##
###
####
###
##
#

import struct
import time
inicio = time.time()
print("----------DIVIDINDO E INTERCALANDO...-----------")
registroCEP = struct.Struct("72s72s72s72s2s8s2s")
f = open("cep.dat", "rb")
saida_1 = open('arq_1.dat', 'wb')
saida_2 = open('arq_2.dat', 'wb')
f.seek(0,2)
for i in range(0, 350000):
    
    f.seek(i*endereco.size)    
    linha = f.read(endereco.size)
    
    if i%2==0:
        saida_1.write(linha)        

    if i%2!=0:
        saida_2.write(linha)
f.close()
saida_1.close()
saida_2.close()
f_int = time.time()
print("----------FIM DA INTERCALACAO...-----------")
print("Tempo de intercalaca", f_int - inicio)


print("---------MESCLANDO...----------")
endereco = struct.Struct("72s72s72s72s2s8s2s")
f = open("cep_ord_mesclar.dat", "wb")
f_1 = open('arq_1.dat', 'r')
f_2 = open('arq_2.dat', 'r')
col_CEP = 5
f_1.seek(0, 2)
n_linhas = f_1.tell() / endereco.size

for i in range(0, int(n_linhas)):
    f_1.seek(i*endereco.size)
    f_2.seek(i*endereco.size)
    linha_1 = f_1.read(endereco.size).encode('latin1')
    linha_2 = f_2.read(endereco.size).encode('latin1')
    record_1 = endereco.unpack(linha_1)[col_CEP].decode('latin1')
    record_2 = endereco.unpack(linha_2)[col_CEP].decode('latin1')
    
    if record_1<record_2:
        f.write(linha_1)
        f.write(linha_2)
    else:
        f.write(linha_2)
        f.write(linha_1)
f.close() 
f_1.close()
f_2.close()

f_mesc = time.time()
print("---------FIM DA MESCLAGEM...----------")
print("Tempo total do processo", f_mesc - inicio)