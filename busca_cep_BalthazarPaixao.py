##Balthazar Paixão
#
##
###
####
###
##
#
import struct
import sys
if len(sys.argv) != 2:
    print ("USO %s [CEP]" % sys.argv[0])
    quit()
endereco = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
f = open("cep_ordenado.dat","rb")
line = f.read(endereco.size)
counter = 0

while len(line) == endereco.size:
    line = f.read(endereco.size)
    counter+= 1
f.seek(0)

inicio = 0
fim = counter - 1
i = 0
while(inicio <= fim):
    i +=1
    meio = int((inicio+fim)//2)
    f.seek(meio*300)    
    line = f.read(endereco.size)
    record = endereco.unpack(line)
    cep = str(record[cepColumn],'latin1') 
    if cep == sys.argv[0]:
        break
    elif cep < sys.argv[0]:
        inicio = meio + 1
    else:
        fim = meio - 1    
print(i)
f.close()