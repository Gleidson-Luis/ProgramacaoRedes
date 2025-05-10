#Função para saída de dados
print ("Hello World")

#Como declarar uma variável
valor = 45
print(type(valor))
valor = "IFRN"
print(type(valor))

#Tipos do Python
valor_inteiro = 7568 #Inteiro
valor_real = 458.25 #Float ou real (não usar vírgula, sempre ponto)
valor_logico =True #Valor Lógico
valor_logico = False #Valor Lógico
valor_string = "João" #Valor do tipo string
valor_string = 'IFRN' #Valor do tipo String
valor_lista = [45,23,98] #Valor Lista
valor_tupla = (89,98,98) #Valor tupla
valor_dicionario = {"nome" : "João", "idade" : 45}

valor = int(input("Digite um valor: ")) #Input sempre entrega string (A função int vai pegar o texto e converte para inteiro)
soma = valor + 20
print(soma)