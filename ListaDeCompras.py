import xlsxwriter

file = xlsxwriter.Workbook("lista_de_compras.xlsx")
table = file.add_worksheet("Lista_de_compras")


titulo =("SEJA BEM-VINDO A SUA LISTA DE COMPRAS")
print(titulo)
print(len(titulo)*"-")
observação = ("Para consultar a lista, procure a pasta")
observação2 = ("com o nome Listade contatos contida ")
observação3 = ("Dentro da pasta do programa.")
print(observação)
print(len(titulo)*"-")
print(observação2)
print(len(titulo)*"-")
print(observação3)
print(len(titulo)*"-")




S = ["quantidade"]
N = ["ítem"]

for i in (S) and (N):
  pergunta = input("deseja adicionar algo a lista. S/N? ")
  if pergunta == "S":
      a1 = input("ítem:")
      a2 = input("quantidade:")
        
      N.append(a1)
      S.append(a2)

        
  else:
       y = len(N)
       def fun(x):
           if x < 1:
               return 0
           else:
               x = (x-1)
               print("foram cadastrados "+str(x)+" processos.")

       fun(y)
       for i in range(len(S)) and range(len(N)):
           table.write(i,0,S[i]+"\n")
           table.write(i,1,N[i]+"\n")
       
      
file.close()     



